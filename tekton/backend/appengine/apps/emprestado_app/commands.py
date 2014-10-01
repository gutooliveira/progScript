# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode, CreateArc, DeleteArcs, SingleOriginSearch
from emprestado_app.model import Emprestado, ArcoEmprestimo


class EmprestadoPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Emprestado
    _include = [Emprestado.amigo, 
                Emprestado.pertence]


class EmprestadoForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Emprestado
    _include = [Emprestado.amigo, 
                Emprestado.pertence]


class EmprestadoDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Emprestado
    _include = [Emprestado.amigo, 
                Emprestado.pertence, 
                Emprestado.creation]


class EmprestadoShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Emprestado
    _include = [Emprestado.amigo, 
                Emprestado.pertence, 
                Emprestado.creation]


class SaveEmprestadoCommand(SaveCommand):
    _model_form_class = EmprestadoForm


class UpdateEmprestadoCommand(UpdateNode):
    _model_form_class = EmprestadoForm


class ListEmprestadoCommand(ModelSearchCommand):
    def __init__(self):
        super(ListEmprestadoCommand, self).__init__(Emprestado.query_by_creation())

class SalvarEmprestimo(CreateArc):
    def __init__(self, amigo, **pertences):
        salva_cmd=SaveEmprestadoCommand(**pertences)
        super(SalvarEmprestimo, self).__init__(ArcoEmprestimo, amigo, salva_cmd)

class DeletarEmprestimo(DeleteArcs):
    def __init__(self, amigo):
        super(DeletarEmprestimo, self).__init__(ArcoEmprestimo, destination=amigo)

class GetEmprestimo(SingleOriginSearch):
    def __init__(self, pertences):
        super(GetEmprestimo, self).__init__(ArcoEmprestimo, pertences)