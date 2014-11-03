# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from quero_app.commands import ListQueroCommand, SaveQueroCommand, UpdateQueroCommand, \
    QueroPublicForm, QueroDetailForm, QueroShortForm


def save_quero_cmd(**quero_properties):
    """
    Command to save Quero entity
    :param quero_properties: a dict of properties to save on model
    :return: a Command that save Quero, validating and localizing properties received as strings
    """
    return SaveQueroCommand(**quero_properties)


def update_quero_cmd(quero_id, **quero_properties):
    """
    Command to update Quero entity with id equals 'quero_id'
    :param quero_properties: a dict of properties to update model
    :return: a Command that update Quero, validating and localizing properties received as strings
    """
    return UpdateQueroCommand(quero_id, **quero_properties)


def list_queros_cmd():
    """
    Command to list Quero entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListQueroCommand()


def quero_detail_form(**kwargs):
    """
    Function to get Quero's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return QueroDetailForm(**kwargs)


def quero_short_form(**kwargs):
    """
    Function to get Quero's short form. just a subset of quero's properties
    :param kwargs: form properties
    :return: Form
    """
    return QueroShortForm(**kwargs)

def quero_public_form(**kwargs):
    """
    Function to get Quero'spublic form. just a subset of quero's properties
    :param kwargs: form properties
    :return: Form
    """
    return QueroPublicForm(**kwargs)


def get_quero_cmd(quero_id):
    """
    Find quero by her id
    :param quero_id: the quero id
    :return: Command
    """
    return NodeSearch(quero_id)


def delete_quero_cmd(quero_id):
    """
    Construct a command to delete a Quero
    :param quero_id: quero's id
    :return: Command
    """
    return DeleteNode(quero_id)

