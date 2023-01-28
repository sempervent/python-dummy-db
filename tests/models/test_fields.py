#!/usr/bin/env python3
"""Test the python_dummy_db.models.fields module."""
from python_dummy_db.models.fields import Field


def test_field():
    """Test that Field works as expected."""
    int_field = Field(value=3, data_type=int)
    str_field = Field(value='string', data_type=str)
    int_field.relations(str_field)

