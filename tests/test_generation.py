#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test generation functions."""
from python_dummy_db.generation import randfloat


def test_randfloat():
    """Test the randfloat function."""
    random_float = randfloat(lower_bound=1, upper_bound=9, precision=2)
    assert len(str(random_float)) == 4  # [1-9].xx for 4 total chars
