# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from quero_app import facade
from routes.queros.admin import new, edit


def delete(_handler, quero_id):
    facade.delete_quero_cmd(quero_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_queros_cmd()
    queros = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.quero_short_form()

    def short_quero_dict(quero):
        quero_dct = short_form.fill_with_model(quero)
        quero_dct['edit_path'] = router.to_path(edit_path, quero_dct['id'])
        quero_dct['delete_path'] = router.to_path(delete_path, quero_dct['id'])
        return quero_dct

    short_queros = [short_quero_dict(quero) for quero in queros]
    context = {'queros': short_queros,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

