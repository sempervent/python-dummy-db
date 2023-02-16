#!/usr/bin/env python3
"""Define generic fields."""
# pylint: disable=too-few-public-methods
from typing import Optional, Any, List, Union, Callable, Type
from random import randint, seed
from uuid import uuid4, UUID
from pydantic import BaseModel
from loguru import logger

from python_dummy_db.fxns import noop
from python_dummy_db.types import NoopType
from python_dummy_db.distributions import Distribution


class Field(BaseModel):
    """The Field BaseModel exists to provide as the base for Field
        objects. A Field object can be generated with random data.
    """
    _id: Optional[Union[str, UUID, int]] = uuid4()
    name: Optional[str] = None
    data_type: Type = NoopType
    relations: Optional[List[Any]] = None
    values: Optional[List[Any]] = None
    rand_func: Callable = noop
    seed_func: Callable = seed
    seed_kwargs: Optional[dict] = None
    distribution: Optional[Distribution] = None

    def define_seed(self,
                    seed_func: Optional[Callable] = None,
                    seed_kwargs: Optional[dict] = None):
        """Define the seed and seed_kwargs to use.
        Args:
            seed_func: optional function to be used to set the seed
            seed_kwargs: optional default arguments to be supplied to seed_func
        """
        if seed_func is not None and callable(seed_func):
            self.seed_func = seed_func
        if isinstance(seed_kwargs, dict):
            self.seed_kwargs = seed_kwargs
        # pylint: disable=comparison-with-callable
        if self.seed_kwargs is None and seed_kwargs is None and \
                seed == seed_func:
            self.seed_kwargs = {'a': None}
        # pylint: enable=comparison-with-callable

    def verify(
        self,
    ) -> Optional[bool]:
        """Verify that value data or data is of the type."""
        if isinstance(self.values, list):
            return all(isinstance(value, self.data_type)
                       for value in self.values)
        return None

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
        seed_kwargs: Optional[dict] = None,
        **kwargs,
    ) -> Optional[list]:
        """Generate N random values from min to max."""
        # pylint: disable=too-many-boolean-expressions
        print(f'{args=}')
        print(f'{kwargs=}')
        if (return_values is False and store is False and append is False) \
                or (rand_func is None and self.rand_func is None) \
                or (self.rand_func == noop or not callable(self.rand_func)) \
                or (not isinstance(N, int) or N < 1) \
                or (not args and not kwargs):
            return None
        # pylint: enable=too-many-boolean-expressions
        values = []
        for _ in range(N):
            if seed_kwargs and callable(self.seed_func):
                self.seed_func(**seed_kwargs)
            elif isinstance(self.seed_kwargs, dict) and \
                    callable(self.seed_func):
                self.seed_func(**self.seed_kwargs)
            if rand_func is not None and callable(rand_func):
                values.append(rand_func(*args, **kwargs))
            elif (self.rand_func is not None and self.rand_func != noop) \
                    and callable(self.rand_func):
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
    rand_func: Callable = randint
