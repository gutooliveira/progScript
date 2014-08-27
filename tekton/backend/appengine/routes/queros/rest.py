# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from quero_app import facade


def index():
    cmd = facade.list_queros_cmd()
    quero_list = cmd()
    short_form=facade.quero_short_form()
    quero_short = [short_form.fill_with_model(m) for m in quero_list]
    return JsonResponse(quero_short)


def save(**quero_properties):
    cmd = facade.save_quero_cmd(**quero_properties)
    return _save_or_update_json_response(cmd)


def update(quero_id, **quero_properties):
    cmd = facade.update_quero_cmd(quero_id, **quero_properties)
    return _save_or_update_json_response(cmd)


def delete(quero_id):
    facade.delete_quero_cmd(quero_id)()


def _save_or_update_json_response(cmd):
    try:
        quero = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.quero_short_form()
    return JsonResponse(short_form.fill_with_model(quero))

