# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from quero_app import facade
from routes.queros import admin


@no_csrf
def index(quero_id):
    quero = facade.get_quero_cmd(quero_id)()
    detail_form = facade.quero_detail_form()
    context = {'save_path': router.to_path(save, quero_id), 'quero': detail_form.fill_with_model(quero)}
    return TemplateResponse(context, 'queros/admin/form.html')


def save(_handler, quero_id, **quero_properties):
    cmd = facade.update_quero_cmd(quero_id, **quero_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'quero': cmd.form}

        return TemplateResponse(context, 'queros/admin/form.html')
    _handler.redirect(router.to_path(admin))

