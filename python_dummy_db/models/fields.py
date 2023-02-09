#!/usr/bin/env python3
"""Define generic fields."""
# pylint: disable=too-few-public-methods
from typing import Optional, Any, List, Union, Callable
from random import randint
from uuid import uuid4, UUID
from pydantic import BaseModel, SecretStr
from loguru import logger

from python_dummy_db.fxns import noop


class Field(BaseModel):
    """The Field BaseModel exists to provide as the base for Field
        objects. A Field object can be generated with random data.
    """
    _id: Optional[Union[str, UUID, int]] = uuid4()
    value: Optional[Any] = None
    data_type: Optional[Any] = None
    relations: Optional[List[Any]] = None
    values: Optional[List[Any]] = None
    rand_func: Callable = noop

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

    # pylint: disable=too-many-arguments,too-many-branches
    def generate_values(
        self, *args, N: int = 1,
        store: bool = True,
        return_values: bool = False,
        append: bool = True,
        rand_func: Optional[Callable] = None,
        **kwargs,
    ) -> Optional[list]:
        """Generate N random values from min to max."""
        if return_values is False and store is False and append is False:
            return None
        if rand_func is None and self.rand_func is None:
            return None
        if N < 1:
            return None
        values = []
        for _ in range(N):
            if rand_func is not None and callable(rand_func):
                values.append(rand_func(*args, **kwargs))
            elif self.rand_func is not None and callable(self.rand_func):
                values.append(self.rand_func(*args, **kwargs))
            else:
                logger.warning(
                    'No rand_func specified in self or as argument.')
        if append is True:
            if self.values is None:
                self.values = []
            self.values.extend(values)
        elif store is True:
            if len(values) > 1:
                self.values = values
            else:
                self.values = [values]
        if return_values is True:
            return values
        return None
    # pylint: enable=too-many-arguments,too-many-branches


class IntegerField(Field):
    """An Integer field."""
    value: int
    random_func: Callable = randint

