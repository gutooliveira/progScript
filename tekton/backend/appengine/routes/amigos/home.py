# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from amigo_app import facade
from routes.amigos import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_amigos_cmd()
    amigos = cmd()
    public_form = facade.amigo_public_form()
    amigo_public_dcts = [public_form.fill_with_model(amigo) for amigo in amigos]
    context = {'amigos': amigo_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

