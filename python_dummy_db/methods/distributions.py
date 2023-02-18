#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Provide distribution generation models."""
from typing import List, Union, Optional

import numpy as np

from python_dummy_db.types import NumericType


def distribute_equal(
    population_size: int,
    total_resource: float,
) -> List[float]:
    """Distribute amount among size equally."""
    return [total_resource / population_size for i in range(population_size)]


def distribute_gaussian(
    population_size: int,
    total_resource: float,
) -> List[float]:
    """Distribute amount with a gaussian distribution."""
    mean = total_resource / population_size
    std = mean / 4
    return list(np.random.normal(mean, std, population_size))


def distribute_binomial(
    population_size: int,
    total_resource: float,
    p: float = 0.5,
) -> List[float]:
    """Distribute amount with a binomial distribution."""
    return list(
        np.random.binomial(total_resource, p, size=population_size)
    )


def distribute_poisson(
    population_size: int,
    total_resource: float,
) -> List[float]:
    """Distribute amount with a poisson distribution."""
    mean = total_resource / population_size
    return list(
        np.random.poisson(mean, size=population_size)
    )


def distribute_exponential(
    population_size: int,
    total_resource: float,
) -> List[float]:
    """Distribute amount with an exponential distribution."""
    scale = total_resource / population_size
    return list(
        np.random.exponential(scale, size=population_size)
    )


def distribute_uniform(
    population_size: int,
    total_resource: float,
) -> List[float]:
    """Distribute amount with an uniform distribution."""
    low = total_resource / population_size / 2
    high = total_resource / population_size * 2
    return list(
        np.random.uniform(low, high, population_size)
    )


def distribute_beta(
    population_size: int,
    total_resource: float,
    alpha: Optional[Union[float, List[Union[NumericType]]]] = None,
    beta: Optional[Union[float, List[Union[NumericType]]]] = None,
) -> List[float]:
    """Distribute amount with a beta distribution."""
    if alpha is None and beta is None:
        mean = total_resource / population_size
        variance = mean * (1 - mean) / (population_size - 1)
        if alpha is None:
            alpha = mean * ((mean * (1 - mean)) / variance - 1)
        if beta is None:
            beta = (1 - mean) * ((mean * (1 - mean)) / variance - 1)
            if beta <= 0:
                beta = population_size - total_resource
            if beta <= 0:
                beta = total_resource / population_size
            print(f'{beta=}')
    return list(
        np.random.beta(alpha, beta, population_size)
    )


def distribute_chisquare(
    population_size: int,
    total_resource: float,
    df: Optional[Union[float, List[Union[NumericType]]]] = None,
) -> List[float]:
    """Distribute amount with a chisquare distribution."""
    if df is None:
        df = 1 / (2 * (1 / total_resource))
    return list(
        np.random.chisquare(df=df, size=population_size)
    )


DISTRIBUTION_SWITCH = {
    'equal': distribute_equal,
    'gaussian': distribute_gaussian,
    'binomial': distribute_binomial,
    'poisson': distribute_poisson,
    'exponential': distribute_exponential,
    'uniform': distribute_uniform,
    'beta': distribute_beta,
    'chisquare': distribute_chisquare,
}
