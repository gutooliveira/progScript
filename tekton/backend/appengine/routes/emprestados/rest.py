# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from emprestado_app import facade


def index():
    cmd = facade.list_emprestados_cmd()
    emprestado_list = cmd()
    short_form=facade.emprestado_short_form()
    emprestado_short = [short_form.fill_with_model(m) for m in emprestado_list]
    return JsonResponse(emprestado_short)


def save(**emprestado_properties):
    cmd = facade.save_emprestado_cmd(**emprestado_properties)
    return _save_or_update_json_response(cmd)


def update(emprestado_id, **emprestado_properties):
    cmd = facade.update_emprestado_cmd(emprestado_id, **emprestado_properties)
    return _save_or_update_json_response(cmd)


def delete(emprestado_id):
    facade.delete_emprestado_cmd(emprestado_id)()


def _save_or_update_json_response(cmd):
    try:
        emprestado = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.emprestado_short_form()
    return JsonResponse(short_form.fill_with_model(emprestado))

