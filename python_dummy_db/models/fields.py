#!/usr/bin/env python3
"""Define generic fields."""
# pylint: disable=too-few-public-methods
from typing import Optional, Any, List, Union, Callable
from random import randint
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
    values: Optional[List[Any]] = None
    rand_func: Optional[Callable] = None

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

    # pylint: disable=too-many-arguments
    def generate_values(
        self, N: int = 0, min_num: int = 0, max_num: int = 100,
        store: bool = True, return_values: bool = False,
        append: bool = True,
    ) -> Optional[list]:
        """Generate N random values from min to max."""
        if return_values is False and store is False and append is False:
            return None
        if N < 1:
            return None
        values = []
        for _ in range(N):
            values.append(self.random_func(min_num, max_num))
        if append is True:
            self.values.extend(values)
        if store is True and append is False:
            self.values = values
        if return_values is True:
            return values
        return None
    # pylint: enable=too-many-arguments


class IntegerField(Field):
    """An Integer field."""
    value: int
    random_func: Callable = randint

