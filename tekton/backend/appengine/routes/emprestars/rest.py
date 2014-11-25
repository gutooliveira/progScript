# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from emprestar_app.model import ArcoLogado, Emprestar
from gaebusiness.business import CommandExecutionException
from gaegraph.business_base import CreateArc, DeleteArcs
from tekton.gae.middleware.json_middleware import JsonResponse
from emprestar_app import facade


def index():
    cmd = facade.list_emprestars_cmd()
    emprestar_list = cmd()
    short_form=facade.emprestar_short_form()
    emprestar_short = [short_form.fill_with_model(m) for m in emprestar_list]
    return JsonResponse(emprestar_short)


def save(_logged_user, **emprestar_properties):
    cmd = facade.save_emprestar_cmd(**emprestar_properties)
    pertence = cmd()
    CreateArc(arc_class=ArcoLogado, origin=_logged_user, destination=pertence)()
    return _save_or_update_json_response(cmd)


def update(emprestar_id, **emprestar_properties):
    cmd = facade.update_emprestar_cmd(emprestar_id, **emprestar_properties)
    return _save_or_update_json_response(cmd)


def delete(_logged_user, emprestar_id):
    pertence = Emprestar.get_by_id(emprestar_id)
    DeleteArcs(arc_class=ArcoLogado, origin=_logged_user, destination=pertence)()
    facade.delete_emprestar_cmd(emprestar_id)()
    return JsonResponse({'id': emprestar_id})


def edit(**emprestar_properties):
    emprestar_id = emprestar_properties['emprestar_id']
    pertence = Emprestar.get_by_id(emprestar_properties['emprestar_id'])
    emprestar_properties.pop('emprestar_id')
    pertence.populate(**emprestar_properties)
    pertence.put()
    return JsonResponse({'id': emprestar_id})

def _save_or_update_json_response(cmd):
    try:
        emprestar = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.emprestar_short_form()
    return JsonResponse(short_form.fill_with_model(emprestar))

