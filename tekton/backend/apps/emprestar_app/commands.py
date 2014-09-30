# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode, CreateArc, DeleteArcs
from emprestar_app.model import Emprestar, ArcoLogado


class EmprestarPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Emprestar
    _include = [Emprestar.emprestar, 
                Emprestar.pertence, 
                Emprestar.descricao, 
                Emprestar.nome]


class EmprestarForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Emprestar
    _include = [Emprestar.emprestar, 
                Emprestar.pertence, 
                Emprestar.descricao, 
                Emprestar.nome]


class EmprestarDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Emprestar
    _include = [Emprestar.emprestar, 
                Emprestar.pertence, 
                Emprestar.creation, 
                Emprestar.descricao, 
                Emprestar.nome]


class EmprestarShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Emprestar
    _include = [Emprestar.emprestar, 
                Emprestar.pertence, 
                Emprestar.creation, 
                Emprestar.descricao, 
                Emprestar.nome]


class SaveEmprestarCommand(SaveCommand):
    _model_form_class = EmprestarForm


class UpdateEmprestarCommand(UpdateNode):
    _model_form_class = EmprestarForm


class ListEmprestarCommand(ModelSearchCommand):
    def __init__(self):
        super(ListEmprestarCommand, self).__init__(Emprestar.query_by_creation())


class SalvarPertence(CreateArc):
    def __init__(self, user, **pertences):
        salva_cmd=SaveEmprestarCommand(**pertences)
        super(SalvarPertence, self).__init__(ArcoLogado, user, salva_cmd)

class DeletarPertence(DeleteArcs):
    def __init__(self, user):
        super(DeletarPertence, self).__init__(ArcoLogado, destination=user)
