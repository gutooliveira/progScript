# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from amigo_app.model import Amigo
from config.template_middleware import TemplateResponse
from emprestado_app.commands import GetEmprestimo
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from emprestado_app import facade
from routes.emprestados import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'emprestados/admin/form.html')


def save(_handler, _logged_user, emprestado_id=None,**emprestado_properties):



    cmd = facade.save_emprestado_cmd(**emprestado_properties)

    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'emprestado': cmd.form}

        return TemplateResponse(context, 'emprestados/admin/form.html')
    _handler.redirect(router.to_path(admin))

