#!/usr/bin/env python3
"""Test the python_dummy_db.distributions module."""
from pandas import DataFrame

from python_dummy_db.distributions import Distribution

from tests.test_data.distributions import (
    WEALTH_PER_PERSON,
    WEALTH_PER_PERSON_WITH_UNITS,
    DISTRIBUTIONS,
)


def test_distribution_class():
    """Test functional requirements of the Distribution class."""
    d = Distribution(**WEALTH_PER_PERSON)
    # test all methods for the wealth figures
    wealth_per_person = {
        'equal': d.equal(),
        'left_skewed': d.left_skewed(),
        'right_skewed':  d.right_skewed(),
        'log_normal': d.log_normal(),
        'exponential': d.exponential(),
        'pareto': d.pareto(),
        'gaussian': d.gaussian(),
        'binomial': d.binomial(),
        'poisson': d.poisson(),
        'uniform': d.uniform(),
    }
    for key, value in wealth_per_person.items():
        # ensure that that each call to the distribution is a DataFrame
        assert isinstance(value, DataFrame) is True
        assert key in DISTRIBUTIONS  # test the test
    # create using distribution method
    wealth_per_person_via_distribution = {}
    for distribution in DISTRIBUTIONS:
        wealth_per_person_via_distribution[distribution] = \
            d.distribution(dist_type=distribution)  # update the dict
    assert wealth_per_person_via_distribution == wealth_per_person
    for distribution in DISTRIBUTIONS:
        assert wealth_per_person[distribution] == \
            wealth_per_person_via_distribution[distribution]
