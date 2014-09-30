# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from amigo_app import facade
from routes.amigos import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'amigos/admin/form.html')


def save(_handler, amigo_id=None, **amigo_properties):
    cmd = facade.save_amigo_cmd(**amigo_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'amigo': cmd.form}

        return TemplateResponse(context, 'amigos/admin/form.html')
    _handler.redirect(router.to_path(admin))

