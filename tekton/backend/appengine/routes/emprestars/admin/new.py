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


def save(_handler,_logged_user, emprestar_id=None,**emprestar_properties):
    #cmd = facade.save_emprestar_cmd(**emprestar_properties)
    cmd_user=facade.SalvarPertence(_logged_user,**emprestar_properties)
    try:
        cmd_user()
    except CommandExecutionException:
        context = {'errors': cmd_user.errors,
                   'emprestar': cmd_user.form}

        return TemplateResponse(context, 'emprestars/admin/form.html')
    _handler.redirect(router.to_path(admin))

