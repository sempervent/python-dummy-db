#!/usr/bin/env python3
"""Test the python_dummy_db.distributions module."""
import pytest
import numpy as np

from python_dummy_db.types import NumericType
from python_dummy_db.distributions import Distribution
from python_dummy_db.methods.distributions import DISTRIBUTION_SWITCH as DS

from tests.test_data.distributions import (
    WEALTH_PER_PERSON,
    DISTRIBUTION_TEST_DATA as DTD,
)


def test_distribution_class():
    """Test functional requirements of the Distribution class."""
    d = Distribution(**WEALTH_PER_PERSON)
    # test all methods for the wealth figures
    wealth_per_person = {}
    for key in DS:  # iterate over the available distributions
        wealth_per_person[key] = d.distribute(distribution=key,
                                              give_value=True)
    for key, value in wealth_per_person.items():
        # ensure that that each call to the distribution is a DataFrame
        assert isinstance(value, list) is True
        assert key in DS  # test the test


@pytest.mark.parametrize("distribution", DS.keys(), ids=DS.keys())
@pytest.mark.parametrize("seed_data", DTD.values(), ids=DTD.keys())
def test_distribution_insights(distribution, seed_data):
    """Test the functional requirements of the Distribution class."""
    d = Distribution(**seed_data)
    d.distribute(distribution=distribution)
    assert isinstance(d.population_distribution, list)
    assert len(d.population_distribution) == d.population_size
    assert isinstance(d.mean_allocation(), NumericType)
    assert isinstance(d.standard_deviation(), NumericType)
    assert isinstance(d.min_allocation(), NumericType)
    assert isinstance(d.max_allocation(), NumericType)
    assert isinstance(d.cumulative_distribution(), np.ndarray)
    assert isinstance(d.percentile_allocations(), NumericType)
