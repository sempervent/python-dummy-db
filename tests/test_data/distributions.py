#!/usr/bin/env python3
"""Provide distribution data for test cases."""

PERCENTAGES = [
    0.001, 0.01, 0.05, 0.1, 0.15, 0.2, 0.25, 0.33, 0.5, 0.75, 0.9, 1
]

DISTRIBUTIONS = ['equal', 'left_skewed', 'right_skewed', 'log_normal',
                 'exponential', 'pareto', 'guassian', 'binomial', 'poisson',
                 'uniform']

WEALTH_PER_PERSON = {  # wealth per person example using 2021 data from ChatGPT
    "n": (7.9 * 1e9),  # 7.9 billion people in the world
    "amount": (440 * 1e12),  # 440 trillion wealth in the world
    "percentages": PERCENTAGES,
}

WEALTH_PER_PERSON_WITH_UNITS = {
    **WEALTH_PER_PERSON,
    "use_units": True,  # force to strings and use units
    "unit": "Wealth ($)",  # the amount is total wealth, this is that unit
    "n_unit": "People",  # n represents all the people in the world
}

DEBT_PER_PERSON = {  # debt per person
    "n": (8.0 * 1e9),  # 8 billion people in the world
    "amount": (300 * 1e12),  # 300 trillion debt
    "percentages": PERCENTAGES,
}

DEBT_PER_PERSON_WITH_UNITS = {
    **DEBT_PER_PERSON,
    "use_units": True,  # force to strings and use units
    "unit": "Debt ($)",  # the amount is total debt, this is the unit
    "n_unit": "People",  # n represents all the people in the world
}
