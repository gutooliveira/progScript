# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from quero_app import facade
from routes.queros import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_queros_cmd()
    queros = cmd()
    public_form = facade.quero_public_form()
    quero_public_dcts = [public_form.fill_with_model(quero) for quero in queros]
    context = {'queros': quero_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

