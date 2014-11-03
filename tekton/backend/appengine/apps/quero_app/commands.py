# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from quero_app.model import Quero

class QueroPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Quero
    _include = [Quero.item, 
                Quero.descricao, 
                Quero.nome]


class QueroForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Quero
    _include = [Quero.item, 
                Quero.descricao, 
                Quero.nome]


class QueroDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Quero
    _include = [Quero.item, 
                Quero.creation, 
                Quero.descricao, 
                Quero.nome]


class QueroShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Quero
    _include = [Quero.item, 
                Quero.creation, 
                Quero.descricao, 
                Quero.nome]


class SaveQueroCommand(SaveCommand):
    _model_form_class = QueroForm


class UpdateQueroCommand(UpdateNode):
    _model_form_class = QueroForm


class ListQueroCommand(ModelSearchCommand):
    def __init__(self):
        super(ListQueroCommand, self).__init__(Quero.query_by_creation())

