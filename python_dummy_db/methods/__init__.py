#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Allow imports from this directory."""
from python_dummy_db.methods.distributions import DISTRIBUTION_SWITCH


def show_help(*args, **kwargs):
    """Show help for the Distribution Switch if called."""
    swallowed_arguments = "Swallowed:\n"
    if args:
        swallowed_arguments += f'\t{args=}\n'
    if kwargs:
        swallowed_arguments += f'\t{kwargs=}\n'
    if not swallowed_arguments.endswith(':\n'):
        print(f'`show_help` {swallowed_arguments}')


DISTRIBUTION_SWITCH.update({'help': show_help})
