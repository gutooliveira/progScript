# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from emprestar_app.commands import ListEmprestarCommand, SaveEmprestarCommand, UpdateEmprestarCommand, \
    EmprestarPublicForm, EmprestarDetailForm, EmprestarShortForm, SalvarPertence, DeletarPertence


def save_emprestar_cmd(**emprestar_properties):
    """
    Command to save Emprestar entity
    :param emprestar_properties: a dict of properties to save on model
    :return: a Command that save Emprestar, validating and localizing properties received as strings
    """
    return SaveEmprestarCommand(**emprestar_properties)


def update_emprestar_cmd(emprestar_id, **emprestar_properties):
    """
    Command to update Emprestar entity with id equals 'emprestar_id'
    :param emprestar_properties: a dict of properties to update model
    :return: a Command that update Emprestar, validating and localizing properties received as strings
    """
    return UpdateEmprestarCommand(emprestar_id, **emprestar_properties)


def list_emprestars_cmd():
    """
    Command to list Emprestar entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListEmprestarCommand()


def emprestar_detail_form(**kwargs):
    """
    Function to get Emprestar's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return EmprestarDetailForm(**kwargs)


def emprestar_short_form(**kwargs):
    """
    Function to get Emprestar's short form. just a subset of emprestar's properties
    :param kwargs: form properties
    :return: Form
    """
    return EmprestarShortForm(**kwargs)

def emprestar_public_form(**kwargs):
    """
    Function to get Emprestar'spublic form. just a subset of emprestar's properties
    :param kwargs: form properties
    :return: Form
    """
    return EmprestarPublicForm(**kwargs)


def get_emprestar_cmd(emprestar_id):
    """
    Find emprestar by her id
    :param emprestar_id: the emprestar id
    :return: Command
    """
    return NodeSearch(emprestar_id)


def delete_emprestar_cmd(emprestar_id):
    """
    Construct a command to delete a Emprestar
    :param emprestar_id: emprestar's id
    :return: Command
    """
    return DeleteNode(emprestar_id)

def salvar_emprestimo(user, **pertences):

    return SalvarPertence(user, **pertences)

def delete_arco(user):
    return DeletarPertence(user)