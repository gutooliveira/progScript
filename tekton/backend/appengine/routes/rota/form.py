from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton import router
from tekton.router import to_path

__author__ = 'LuizAugusto'
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

@login_not_required
@no_csrf
def index():
    contexto = {'save_path': router.to_path(salvar)}
    return TemplateResponse()

@login_not_required
def salvar(_resp, nome):
    _resp.write(nome)
