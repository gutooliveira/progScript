# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from emprestar_app import facade
from routes.emprestars import admin


@no_csrf
def index(emprestar_id):
    emprestar = facade.get_emprestar_cmd(emprestar_id)()
    detail_form = facade.emprestar_detail_form()
    context = {'save_path': router.to_path(save, emprestar_id), 'emprestar': detail_form.fill_with_model(emprestar)}
    return TemplateResponse(context, 'emprestars/admin/form.html')


def save(_handler, emprestar_id, **emprestar_properties):
    cmd = facade.update_emprestar_cmd(emprestar_id, **emprestar_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'emprestar': cmd.form}

        return TemplateResponse(context, 'emprestars/admin/form.html')
    _handler.redirect(router.to_path(admin))

