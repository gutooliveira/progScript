__author__ = 'GutoOliveira'
# -*- coding: utf-8 -*-
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton import router


@login_not_required
@no_csrf
def index(_handler):
    path = router.to_path(func)
    _handler.redirect(path)


@login_not_required
@no_csrf
def func(_resp, nome, sobrenome='Oliveira'):
    _resp.write('%s %s' % (nome, sobrenome))