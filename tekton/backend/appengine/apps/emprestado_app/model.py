# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from emprestar_app.model import Emprestar
from gaegraph.model import Node, Arc
from gaeforms.ndb import property


class Emprestado(Node):
    amigo = ndb.StringProperty(required=True)
    pertence = ndb.StringProperty(required=True)

class ArcoEmprestimo(Arc):
    destination = ndb.KeyProperty(Emprestar, required=True)