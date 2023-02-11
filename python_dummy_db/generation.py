#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fxns used to generate objects, generally as the `rand_func` argument to
Field types."""
from random import seed, randint
from typing import Optional, Union

from python_dummy_db.types import SeedType


def randfloat(
    lower_bound: int = 0,
    upper_bound: int = 1,
    precision: int = 1,
    seed_: Optional[Union[SeedType + (bool, )]] = None,
) -> Optional[float]:
    """Generate a random float.
    Args:
        lower_bound: int representing the lowest number to pool from
        upper_bound: int representing the highest number to pool from
        precision: int number of digits past decimal place
        seed: optional SeedType class to use or True to generate each time
    Returns:
        if successful a float with the specified inputs, otherwise None
    """
    if isinstance(seed_, SeedType) and seed_ is not None:
        seed(seed_)
    if isinstance(seed_, bool) and seed_ is True:
        seed()
    decimals = []
    number = randint(lower_bound, upper_bound)
    for _ in range(precision):
        if isinstance(seed_, bool) and seed_ is True:
            seed()
        decimals.append(randint(0, 9))
    decimal_places = "."
    decimal_places += "".join(str(decimal) for decimal in decimals)
    return number + float(decimal_places)
