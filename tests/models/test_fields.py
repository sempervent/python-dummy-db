#!/usr/bin/env python3
"""Test the python_dummy_db.models.fields module."""
from random import choice, randint
from python_dummy_db.models.fields import Field


def test_field_creation():
    """Test that Field works as expected."""
    int_field = Field(value=3, data_type=int, rand_func=randint)
    str_field = Field(value='string', data_type=str, rand_func=choice)
    # assert that created values are Field objects
    assert isinstance(int_field, Field) is True
    assert isinstance(str_field, Field) is True
    # assert that value and data_type are the correct
    assert isinstance(int_field.value, int_field.data_type) is True
    assert isinstance(str_field.value, str_field.data_type) is True
    # ensure random values can be generated
    int_field.generate_values(1, 10, N=3)
    assert len(int_field.values) == 3

