#!/usr/bin/python
"""
setup.py for storyline
"""
from setuptools import setup

setup(
    name='storyline',
    version='0.1.0-dev',
    license='MIT',
    description=__doc__.strip(),
    authors='Patricia Wright, Danielle Church',
    author_email='trysha@gmail.com,dani.church@gmail.com',
    packages=['storyline'],
    include_package_data=True,
    install_requires=[
        'Flask>=0.12.2',
    ],
)
