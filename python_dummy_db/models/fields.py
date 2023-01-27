#!/usr/bin/env python3
"""Define generic fields."""
from typing import Optional, Any, List, Union
from uuid4 import uuid4, UUID
from pydantic import BaseModel


class Auth(BaseModel):
    """An Auth object to authenticate with."""




class Schema(BaseModel):
    """Provide the Schema to connect to."""
    auth: Optional[Auth]=None

class Field(BaseModel):
    """The Field BaseModel exists to provide as the base for Field
        objects. A Field object can be generated with random data.
    """
    _id: Optional[Union[str, UUID, int]] = uuid4()
    value: Optional[Any] = None
    data_type: Optional[Any] = None
    relations: Optional[List[Any]] = None

    def relation(self, new_relation: Any):
        """Create a new relationships object and existing relations.
        Args:
            new_relation: any object to relate to this field
        """
        if isinstance(self.relations, list):
            for relation in self.relations:
                relation.relations.append(new_relation)
        if self.relations is None:
            self.relations = []
        self.relations.append(new_relation)


class Table(BaseModel):
    """The Table BaseModel exists to hold a bunch of Fields."""
    schema: Optional[Schema] = None
    fields: Optional[List[Any]] = None

    def field(self, field: Field):
        if self.fields is None:
            self.fields = []
        self.fields.append(field)
