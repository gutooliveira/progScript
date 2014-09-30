# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from emprestado_app import facade
from routes.emprestados import admin


@no_csrf
def index(emprestado_id):
    emprestado = facade.get_emprestado_cmd(emprestado_id)()
    detail_form = facade.emprestado_detail_form()
    context = {'save_path': router.to_path(save, emprestado_id), 'emprestado': detail_form.fill_with_model(emprestado)}
    return TemplateResponse(context, 'emprestados/admin/form.html')


def save(_handler, emprestado_id, **emprestado_properties):
    cmd = facade.update_emprestado_cmd(emprestado_id, **emprestado_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'emprestado': cmd.form}

        return TemplateResponse(context, 'emprestados/admin/form.html')
    _handler.redirect(router.to_path(admin))

