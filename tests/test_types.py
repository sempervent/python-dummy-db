#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test the python_dummy_db.types module."""
from pytest import fail
from python_dummy_db.types import NoopType


# pylint: disable=broad-except
def test_nooptype():
    """Test that the nooptype does nothing."""
    try:
        noop_type = NoopType()
        assert isinstance(noop_type, NoopType) is True
    except Exception as exp:
        fail(f'NoopType failure: {str(exp)}')
# pylint: enable=broad-except
