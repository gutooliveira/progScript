# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from emprestar_app.model import ArcoLogado
from gaebusiness.business import CommandExecutionException
from gaegraph.business_base import CreateArc
from gaepermission.decorator import login_required
from tekton import router
from gaecookie.decorator import no_csrf
from emprestar_app import facade
from routes.emprestars import admin


@no_csrf
@login_required
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'emprestars/admin/form.html')


def save(_handler, _logged_user, emprestar_id=None,**emprestar_properties):
    cmd = facade.save_emprestar_cmd(**emprestar_properties)
    #cmd_user = facade.SalvarPertence(_logged_user, **emprestar_properties)

    # criar arco
    try:
        #cmd_user()
        pertence = cmd()
        CreateArc(arc_class=ArcoLogado, origin=_logged_user, destination=pertence)()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'emprestar': cmd.form}

        return TemplateResponse(context, 'emprestars/admin/form.html')
    _handler.redirect(router.to_path(admin))

