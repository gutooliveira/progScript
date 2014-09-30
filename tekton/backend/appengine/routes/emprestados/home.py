# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from emprestado_app import facade
from routes.emprestados import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_emprestados_cmd()
    emprestados = cmd()
    public_form = facade.emprestado_public_form()
    emprestado_public_dcts = [public_form.fill_with_model(emprestado) for emprestado in emprestados]
    context = {'emprestados': emprestado_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

