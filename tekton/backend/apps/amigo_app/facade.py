# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from amigo_app.commands import ListAmigoCommand, SaveAmigoCommand, UpdateAmigoCommand, \
    AmigoPublicForm, AmigoDetailForm, AmigoShortForm


def save_amigo_cmd(**amigo_properties):
    """
    Command to save Amigo entity
    :param amigo_properties: a dict of properties to save on model
    :return: a Command that save Amigo, validating and localizing properties received as strings
    """
    return SaveAmigoCommand(**amigo_properties)


def update_amigo_cmd(amigo_id, **amigo_properties):
    """
    Command to update Amigo entity with id equals 'amigo_id'
    :param amigo_properties: a dict of properties to update model
    :return: a Command that update Amigo, validating and localizing properties received as strings
    """
    return UpdateAmigoCommand(amigo_id, **amigo_properties)


def list_amigos_cmd():
    """
    Command to list Amigo entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListAmigoCommand()


def amigo_detail_form(**kwargs):
    """
    Function to get Amigo's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return AmigoDetailForm(**kwargs)


def amigo_short_form(**kwargs):
    """
    Function to get Amigo's short form. just a subset of amigo's properties
    :param kwargs: form properties
    :return: Form
    """
    return AmigoShortForm(**kwargs)

def amigo_public_form(**kwargs):
    """
    Function to get Amigo'spublic form. just a subset of amigo's properties
    :param kwargs: form properties
    :return: Form
    """
    return AmigoPublicForm(**kwargs)


def get_amigo_cmd(amigo_id):
    """
    Find amigo by her id
    :param amigo_id: the amigo id
    :return: Command
    """
    return NodeSearch(amigo_id)


def delete_amigo_cmd(amigo_id):
    """
    Construct a command to delete a Amigo
    :param amigo_id: amigo's id
    :return: Command
    """
    return DeleteNode(amigo_id)

