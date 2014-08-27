# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from emprestar_app import facade
from routes.emprestars import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'emprestars/admin/form.html')


def save(_handler, emprestar_id=None, **emprestar_properties):
    cmd = facade.save_emprestar_cmd(**emprestar_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'emprestar': cmd.form}

        return TemplateResponse(context, 'emprestars/admin/form.html')
    _handler.redirect(router.to_path(admin))

