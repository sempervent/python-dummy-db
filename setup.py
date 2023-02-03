#!/usr/bin/env python3
"""Install the python-dummy-db package."""
from pathlib import Path
from setuptools import setup, find_packages


setup(
    name="python_dummy_db",
    version=Path('VERSION').read_text(encoding='UTF-8'),
    description="Generate dummy databases with some fake data in them.",
    long_description=Path('README.md').read_text(encoding='UTF-8'),
    long_description_content_type='text/markdown',
    author="Joshua N. Grant",
    author_email="jngrant@live.com",
    packages=find_packages(exclude=["tests"]),
    url="https://github.com/sempervent/python-dummy-db",
    install_requires=Path('requirements.txt').read_text(
        encoding='UTF-8').split(r'\n'),
    extras_requrie={
        'dev': Path('requirements-dev.txt').read_text(
            encoding='UTF-8').split(r'\n'),
    },
    include_package_data=True,
    license='GPL-3',
)
