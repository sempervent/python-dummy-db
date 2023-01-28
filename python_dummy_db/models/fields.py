#!/usr/bin/env python3
"""Define generic fields."""
# pylint: disable=too-few-public-methods
from typing import Optional, Any, List, Union
from uuid import uuid4, UUID
from pydantic import BaseModel, SecretStr


class Auth(BaseModel):
    """An Auth object to authenticate with."""
    user: Optional[str] = None
    secret: Union[str, SecretStr]

    def hash(self):
        """Hash the password behind SecretStr."""
        if not isinstance(self.secret, SecretStr):
            self.secret = SecretStr(self.secret)


class Connection(BaseModel):
    """Connection object."""
    auth: Optional[Auth] = None
    protocol: Optional[str] = None
    hostname: Optional[str] = None
    database: Optional[str] = None


class Database(BaseModel):
    """Provide database connection information."""
    connection: Connection


class Schema(BaseModel):
    """Provide the Schema to connect to."""
    database: Optional[Database] = None
    schema: str


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


class Table(BaseModel):
    """The Table BaseModel exists to hold a bunch of Fields."""
    schema: Optional[Schema] = None
    fields: Optional[List[Any]] = None

    def field(self, field: Field):
        if self.fields is None:
            self.fields = []
        self.fields.append(field)
