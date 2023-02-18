#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test distribution generation models."""

from python_dummy_db.methods.distributions import DISTRIBUTION_SWITCH

from tests.test_data.distributions import DISTRIBUTION_TEST_DATA


def test_distributions():
    """Test all the distributions available in the DISTRIBUTION_SWITCH dict."""
    for _d, test_args in DISTRIBUTION_TEST_DATA.items():
        for _e, distribution_func in DISTRIBUTION_SWITCH.items():
            results = distribution_func(**test_args)
            assert isinstance(results, list) is True
            assert len(results) == test_args.get('population_size')
