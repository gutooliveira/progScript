# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from amigo_app.model import Amigo

class AmigoPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Amigo
    _include = [Amigo.email, 
                Amigo.nome]


class AmigoForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Amigo
    _include = [Amigo.email, 
                Amigo.nome]


class AmigoDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Amigo
    _include = [Amigo.creation, 
                Amigo.email, 
                Amigo.nome]


class AmigoShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Amigo
    _include = [Amigo.creation, 
                Amigo.email, 
                Amigo.nome]


class SaveAmigoCommand(SaveCommand):
    _model_form_class = AmigoForm


class UpdateAmigoCommand(UpdateNode):
    _model_form_class = AmigoForm


class ListAmigoCommand(ModelSearchCommand):
    def __init__(self):
        super(ListAmigoCommand, self).__init__(Amigo.query_by_creation())

