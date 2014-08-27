# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from emprestar_app import facade
from routes.emprestars import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_emprestars_cmd()
    emprestars = cmd()
    public_form = facade.emprestar_public_form()
    emprestar_public_dcts = [public_form.fill_with_model(emprestar) for emprestar in emprestars]
    context = {'emprestars': emprestar_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

