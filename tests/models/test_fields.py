#!/usr/bin/env python3
"""Test the python_dummy_db.models.fields module."""
from python_dummy_db.models.fields import Field


def test_field():
    """Test that Field works as expected."""
    int_field = Field(value=3, data_type=int)
    str_field = Field(value='string', data_type=str)
    int_field.relation(str_field)
    assert int_field in str_field.relations
    assert str_field in int_field.relations

