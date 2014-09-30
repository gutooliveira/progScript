# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from emprestado_app import facade
from routes.emprestados.admin import new, edit


def delete(_handler, emprestado_id):
    facade.delete_emprestado_cmd(emprestado_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_emprestados_cmd()
    emprestados = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.emprestado_short_form()

    def short_emprestado_dict(emprestado):
        emprestado_dct = short_form.fill_with_model(emprestado)
        emprestado_dct['edit_path'] = router.to_path(edit_path, emprestado_dct['id'])
        emprestado_dct['delete_path'] = router.to_path(delete_path, emprestado_dct['id'])
        return emprestado_dct

    short_emprestados = [short_emprestado_dict(emprestado) for emprestado in emprestados]
    context = {'emprestados': short_emprestados,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

