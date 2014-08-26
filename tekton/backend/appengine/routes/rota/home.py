from config.template_middleware import TemplateResponse

__author__ = 'GutoOliveira'

# -*- coding: utf-8 -*-

from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required


@login_not_required
@no_csrf
def index(nome='Guto',sobrenome="Oliveira"):
    contexto = {'name': nome, 'lastname': sobrenome}
    return TemplateResponse(contexto)