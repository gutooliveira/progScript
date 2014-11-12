# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from emprestar_app.model import ArcoLogado
from gaegraph.business_base import DestinationsSearch, DeleteArcs
from tekton import router
from gaecookie.decorator import no_csrf
from emprestar_app import facade
from routes.emprestars.admin import new, edit
import json


def delete(_handler, _logged_user, emprestar_id):
    facade.delete_emprestar_cmd(emprestar_id)()
    DeleteArcs(arc_class=ArcoLogado, origin=_logged_user, destination=emprestar_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index(_logged_user):
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.emprestar_short_form()

    #Esse cara retorna os pertences do usuário logado
    emprestars = DestinationsSearch(arc_class=ArcoLogado, origin=_logged_user)()

    def short_emprestar_dict(emprestar):
        emprestar_dct = short_form.fill_with_model(emprestar)
        emprestar_dct['edit_path'] = router.to_path(edit_path, emprestar_dct['id'])
        emprestar_dct['delete_path'] = router.to_path(delete_path, emprestar_dct['id'])
        return emprestar_dct

    short_emprestars = [short_emprestar_dict(emprestar) for emprestar in emprestars]
    context = {'emprestars': json.dumps(short_emprestars),
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

