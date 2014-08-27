# coding=utf-8
from config.template_middleware import TemplateResponse

__author__ = 'GutoOliveira'

# -*- coding: utf-8 -*-

from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required


@login_not_required
@no_csrf
def index():
    class Pertence(object):
        def __init__(self, imagem, nome, desc):
            self.imagem = imagem
            self.nome = nome
            self.desc = desc

    pertences = [
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D'),
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D'),
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D'),
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D'),
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D'),
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D'),
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D'),
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D'),
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D'),
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D'),
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D'),
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D'),
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D'),
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D'),
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D'),
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D'),
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D'),
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D'),
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D'),
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D'),
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D'),
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D'),
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D'),
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D'),
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D'),
        Pertence('/static/img/product/canon.jpg', 'Camera fotografica', 'CANON EOS 40D')
    ]

    contexto = {'pertences': pertences}
    return TemplateResponse(contexto)