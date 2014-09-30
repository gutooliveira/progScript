# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node, Arc
from gaeforms.ndb import property


class Emprestar(Node):
    pertence = ndb.StringProperty(required=True)
    nome = ndb.StringProperty(required=True)
    descricao = ndb.StringProperty(required=True)
    emprestar = ndb.DateProperty(required=True)

class ArcoLogado(Arc):
    destination = ndb.KeyProperty(Emprestar,required=True)
