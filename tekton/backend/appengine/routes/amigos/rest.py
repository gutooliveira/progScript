# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from amigo_app import facade


def index():
    cmd = facade.list_amigos_cmd()
    amigo_list = cmd()
    short_form=facade.amigo_short_form()
    amigo_short = [short_form.fill_with_model(m) for m in amigo_list]
    return JsonResponse(amigo_short)


def save(**amigo_properties):
    cmd = facade.save_amigo_cmd(**amigo_properties)
    return _save_or_update_json_response(cmd)


def update(amigo_id, **amigo_properties):
    cmd = facade.update_amigo_cmd(amigo_id, **amigo_properties)
    return _save_or_update_json_response(cmd)


def delete(amigo_id):
    facade.delete_amigo_cmd(amigo_id)()


def _save_or_update_json_response(cmd):
    try:
        amigo = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.amigo_short_form()
    return JsonResponse(short_form.fill_with_model(amigo))

