# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from emprestado_app.commands import ListEmprestadoCommand, SaveEmprestadoCommand, UpdateEmprestadoCommand, \
    EmprestadoPublicForm, EmprestadoDetailForm, EmprestadoShortForm, SalvarEmprestimo, DeletarEmprestimo, GetEmprestimo


def save_emprestado_cmd(**emprestado_properties):
    """
    Command to save Emprestado entity
    :param emprestado_properties: a dict of properties to save on model
    :return: a Command that save Emprestado, validating and localizing properties received as strings
    """
    return SaveEmprestadoCommand(**emprestado_properties)


def update_emprestado_cmd(emprestado_id, **emprestado_properties):
    """
    Command to update Emprestado entity with id equals 'emprestado_id'
    :param emprestado_properties: a dict of properties to update model
    :return: a Command that update Emprestado, validating and localizing properties received as strings
    """
    return UpdateEmprestadoCommand(emprestado_id, **emprestado_properties)


def list_emprestados_cmd():
    """
    Command to list Emprestado entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListEmprestadoCommand()


def emprestado_detail_form(**kwargs):
    """
    Function to get Emprestado's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return EmprestadoDetailForm(**kwargs)


def emprestado_short_form(**kwargs):
    """
    Function to get Emprestado's short form. just a subset of emprestado's properties
    :param kwargs: form properties
    :return: Form
    """
    return EmprestadoShortForm(**kwargs)

def emprestado_public_form(**kwargs):
    """
    Function to get Emprestado'spublic form. just a subset of emprestado's properties
    :param kwargs: form properties
    :return: Form
    """
    return EmprestadoPublicForm(**kwargs)


def get_emprestado_cmd(emprestado_id):
    """
    Find emprestado by her id
    :param emprestado_id: the emprestado id
    :return: Command
    """
    return NodeSearch(emprestado_id)


def delete_emprestado_cmd(emprestado_id):
    """
    Construct a command to delete a Emprestado
    :param emprestado_id: emprestado's id
    :return: Command
    """
    return DeleteNode(emprestado_id)

def salvar_emprestimo(amigo,**pertences):

    return SalvarEmprestimo(amigo,**pertences)

def delete_arco(amigo):
    return DeletarEmprestimo(amigo)


def get_emprestimo(pertences):

    return GetEmprestimo(pertences)
