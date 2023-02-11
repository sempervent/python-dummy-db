#!/usr/bin/env python3
"""Test the python_dummy_db.models.fields module."""
from string import ascii_letters
from random import randint, seed, choice

from python_dummy_db.generation import randfloat
from python_dummy_db.models.fields import Field


def test_field_creation():
    """Test that Field works as expected."""
    int_field = Field(name='Integer', data_type=int, rand_func=randint)
    str_field = Field(name='String', data_type=str, rand_func=choice)
    broken_field = Field(name='Broken', data_type=float, rand_func=randfloat,
                         values=[1.0, 2, 'a'])
    # assert that created values are Field objects
    assert isinstance(int_field, Field) is True
    assert isinstance(str_field, Field) is True
    assert isinstance(broken_field, Field) is True
    # ensure verify no-ops without values generated
    assert int_field.verify() is None
    # ensure broken field is broken
    assert broken_field.verify() is False
    # ensure random values can be generated
    int_field.generate_values(1, 10, N=3)
    str_field.generate_values(N=3, seq=['a', 'b', 'c'])
    assert len(int_field.values) == 3
    assert len(str_field.values) == 3
    # assert that values and data_type are the correct
    assert int_field.verify() is True
    assert str_field.verify() is True
    # assert that setting seeds work
    seed_kwargs = {'a': 5}
    int_field.define_seed(seed_func=seed, seed_kwargs=seed_kwargs)
    assert int_field.seed_kwargs == seed_kwargs
    # pylint: disable=comparison-with-callable
    assert int_field.seed_func == seed
    # pylint: enable=comparison-with-callable
    int_field.generate_values(1, 10, N=9, append=False)
    assert len(int_field.values) == 9
    assert all(value <= 10 for value in int_field.values) is True
    # make sure generate_values aborts properly if values are not set correctly
    assert int_field.generate_values(N=0) is None  # too low N

    assert str_field.generate_values() is None  # no rand_func set
    str_field.define_seed(
        # reset the seed func and seed_kwargs
        seed_func=choice,
        seed_kwargs=dict(seq=list(ascii_letters)),
    )
    assert str_field.generate_values(append=False, store=False) is None
    assert str_field.generate_values(N=0.0) is None  # no floats for N
    assert str_field.generate_values(N=1.3) is None  # no floats above 1
    assert str_field.generate_values(N='a') is None  # no str for N
