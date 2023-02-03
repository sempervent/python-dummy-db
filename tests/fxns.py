#!/usr/bin/env python3
"""Test the python_dummy_db.fxns module."""
from pytest import fail
from python_dummy_db.fxns import noop


# pylint: disable=broad-except
def test_noop():
    """Test that noop function does nothing."""
    try:
        noop()  # test noop w/ no args & kwargs
        noop(None)  # test noop w/ None
        noop(1, "a", {})  # test noop w/ args of different types
        noop(1, "a", c=2, d="e")  # test w/ mixture
    except Exception as exp:
        fail(f'noop failure: {str(exp)}')
# pylint: enable=broad-except
