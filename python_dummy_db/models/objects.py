#!/usr/bin/env python3
"""Define objects for the databse to use."""
from os import environ
from typing import Optional, Union, List, Any, Callable

from pydantic import BaseModel, SecretStr

from python_dummy_db.fxns import noop
from python_dummy_db.models.fields import Field


class Auth(BaseModel):
    """An Auth object to authenticate with."""
    user: Optional[str] = None
    secret: Union[str, SecretStr]

    def get_secret(self):
        """Retrive the secret value."""
        if not isinstance(self.secret, SecretStr):
            self.hash()
        return self.secret.value()

    def hash(self):
        """Hash the password behind SecretStr."""
        if not isinstance(self.secret, SecretStr):
            self.secret = SecretStr(self.secret)

    def set_env_key(self, key_name: Optional[str] = None):
        """Set the secret into the environment.
        Args:
            key_name: optional envar key name, defaults to user
        """
        if key_name is None and self.user is not None:
            key_name = self.user
        environ[key_name] = self.get_secret()


class Connection(BaseModel):
    """Connection object."""
    auth: Optional[Auth] = None
    protocol: Optional[str] = None
    hostname: Optional[str] = None
    database: Optional[str] = None
    module: Optional[str] = None
    connection_callable: Callable = noop


class Database(BaseModel):
    """Provide database connection information."""
    connection: Connection


class Schema(BaseModel):
    """Provide the Schema to connect to."""
    database: Optional[Database] = None
    schema_name: str


class Table(BaseModel):
    """The Table BaseModel exists to hold a bunch of Fields."""
    schema_name: Optional[Schema] = None
    fields: Optional[List[Any]] = None
    database: Optional[Database] = None

    def field(self, field: Field):
        """Assign a field to the table object."""
        if self.fields is None:
            self.fields = []
        self.fields.append(field)
