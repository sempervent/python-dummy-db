#!/usr/bin/env python3
"""Define generic fields."""
# pylint: disable=too-few-public-methods
from typing import Optional, Any, List, Union
from uuid import uuid4, UUID
from pydantic import BaseModel, SecretStr


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
        if isinstance(self.relations, list) and \
                new_relation not in self.relations:
            for relation in self.relations:
                relation.relations.append(new_relation)
        if self.relations is None:
            self.relations = []
        self.relations.append(new_relation)


class IntegerField(Field):
    """An Integer field."""
    value: int
