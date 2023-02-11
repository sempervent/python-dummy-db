#!/usr/bin/env python3
"""Define types to be used."""


# pylint: disable=unnecessary-pass,too-few-public-methods
class NoopType:
    """Don't do anything with this class."""
    pass
# pylint: enable=unnecessary-pass,too-few-public-methods


NumericType = (int, float)
ByteType = (bytes, bytearray)
SeedType = NumericType + ByteType + (str, type(None))
