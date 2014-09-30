# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from amigo_app import facade
from routes.amigos.admin import new, edit


def delete(_handler, amigo_id):
    facade.delete_amigo_cmd(amigo_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_amigos_cmd()
    amigos = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.amigo_short_form()

    def short_amigo_dict(amigo):
        amigo_dct = short_form.fill_with_model(amigo)
        amigo_dct['edit_path'] = router.to_path(edit_path, amigo_dct['id'])
        amigo_dct['delete_path'] = router.to_path(delete_path, amigo_dct['id'])
        return amigo_dct

    short_amigos = [short_amigo_dict(amigo) for amigo in amigos]
    context = {'amigos': short_amigos,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

