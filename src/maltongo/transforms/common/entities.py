#!/usr/bin/env python

from canari.maltego.message import Entity, EntityField, EntityFieldType, MatchingRule

__author__ = 'Matt Newham'
__copyright__ = 'Copyright 2013, Maltongo Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Matt Newham'
__email__ = 'matt.newham@gmail.com'
__status__ = 'Development'

__all__ = [
    'MaltongoEntity',
    'MyMaltongoEntity'
]

"""
DO NOT EDIT:
The following entity is the base entity type from which all your entities will inherit from. This provides you with the
default namespace that all your entities will use for their unique entity type in Maltego. For example, MyMaltongoEntity will
have an entity type name of maltongo.MyMaltongoEntity. When adding a new entity in Maltego, you will have to specify this
name (maltongo.MyMaltongoEntity) in the 'Unique entity type' field.
"""
class MaltongoEntity(Entity):
    namespace = 'maltongo'


"""
You can specify as many entity fields as you want by just adding an extra @EntityField() decorator to your entities. The
@EntityField() decorator takes the following parameters:
    - name: the name of the field without spaces or special characters except for dots ('.') (required)
    - propname: the name of the object's property used to get and set the value of the field (required, if name contains dots)
    - displayname: the name of the entity as it appears in Maltego (optional)
    - type: the data type of the field (optional, default: EntityFieldType.String)
    - required: whether or not the field's value must be set before sending back the message (optional, default: False)
    - choices: a list of acceptable field values for this field (optional)
    - matchingrule: whether or not the field should be loosely or strictly matched (optional, default: MatchingRule.Strict)
    - decorator: a function that is invoked each and everytime the field's value is set or changed.
TODO: define as many custom fields and entity types as you wish:)
"""    
@EntityField(name='maltongo.fieldN', propname='fieldN', displayname='Field N', matchingrule=MatchingRule.Loose)
@EntityField(name='maltongo.field1', propname='field1', displayname='Field 1', type=EntityFieldType.Integer)
class MyMaltongoEntity(MaltongoEntity):
    """
    Uncomment the line below and comment out the pass if you wish to define a ridiculous entity type name like
    'my.fancy.EntityType'
    """
    # name = my.fancy.EntityType
    pass