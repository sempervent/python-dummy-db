#!/usr/bin/env python3
"""Provide distribution data for test cases."""

PERCENTAGES = [
    0.001, 0.01, 0.05, 0.1, 0.15, 0.2, 0.25, 0.33, 0.5, 0.75, 0.9, 1
]

DISTRIBUTIONS = ['equal', 'left_skewed', 'right_skewed', 'log_normal',
                 'exponential', 'pareto', 'guassian', 'binomial', 'poisson',
                 'uniform']

POPULATION_SIZE = int((8 * 1e9) / (500 * 1e6))  # use .5 billion for testing
TOTAL_WEALTH = 440 * 1e12
TOTAL_DEBT = 300 * 1e12
ANNUAL_FOOD_CONSUMPTIONS = 775 * 1e6  # in tonnes 2020
GLOBAL_ENERGY_PRODUCTION = 1.59 * 10e17  # in killowatts for 2020
ANNUAL_CROP_PRODUCTION = 2.3 * 1e9  # in tonnes 2019
CO2_EMISSIONS = 37 * 1e9  # in tonnes 2019
TOTAL_FIREARMS = 857 * 1e6  # global supply in 2017
PLASTIC_WASTE = 335 * 1e6  # tonnes in 2016
AG_PESTICIDE = 1 * 1e6  # tonnes in 2020
FOOD_WASTE = 2.3 * 1e9  # tonnes in 2020 -- includes supply chain lossage
CRIMINAL_JUSTICE_SPENDING = 500 * 1e9  # total in 2020

AMOUNT_DATA = [
    (TOTAL_WEALTH, 'wealth'),
    (TOTAL_DEBT, 'debt'),
    (ANNUAL_FOOD_CONSUMPTIONS, 'yearly-food-consumption'),
    (GLOBAL_ENERGY_PRODUCTION, 'yearly-energy-production'),
    (ANNUAL_CROP_PRODUCTION, 'yearly-crop-production'),
    (CO2_EMISSIONS, 'yearly-co2-emissions'),
    (TOTAL_FIREARMS, 'firearms'),
    (PLASTIC_WASTE, 'plastic-waste'),
    (AG_PESTICIDE, 'ag-pesticide'),
    (FOOD_WASTE, 'food-waste'),
    (CRIMINAL_JUSTICE_SPENDING, 'criminal-justice-spending'),
]

DISTRIBUTION_TEST_DATA = {}
for amount, name in AMOUNT_DATA:
    DISTRIBUTION_TEST_DATA[name] = {
        'population_size': POPULATION_SIZE,
        'total_resource': amount,
    }


WEALTH_PER_PERSON = {  # wealth per person example using 2021 data from ChatGPT
    "population_size": POPULATION_SIZE,
    "total_resource": (440 * 1e12),  # 440 trillion wealth in the world
    "percentages": PERCENTAGES,
}

WEALTH_PER_PERSON_WITH_UNITS = {
    **WEALTH_PER_PERSON,
    "use_units": True,  # force to strings and use units
    "unit": "Wealth ($)",  # the amount is total wealth, this is that unit
    "population_unit": "People",  # n represents all the people in the world
}

DEBT_PER_PERSON = {  # debt per person
    "population_size": POPULATION_SIZE,
    "total_resource": (300 * 1e12),  # 300 trillion debt
    "percentages": PERCENTAGES,
}

DEBT_PER_PERSON_WITH_UNITS = {
    **DEBT_PER_PERSON,
    "use_units": True,  # force to strings and use units
    "unit": "Debt ($)",  # the amount is total debt, this is the unit
    "population_unit": "People",  # n represents all the people in the world
}
