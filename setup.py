#!/usr/bin/env python
# coding=utf-8
"""Project setup."""
import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()

REQUIREMENTS = [
]

TEST_REQUIREMENTS = [
    'pylama==7.0.4',
    'pytest==2.7.2',
]

setup(
    name='returns',
    version='0.0.1',
    description='A decorator to create namedtuples for return values',
    long_description=README,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2 :: Only',
    ],
    keywords='namedtuple return',
    author='Michał Pawłowski',
    author_email='@'.join(['unittestablecode', 'gmail.com']),
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=REQUIREMENTS,
    tests_require=TEST_REQUIREMENTS,
    extras_require={'tests': TEST_REQUIREMENTS},
    cmdclass={},
    entry_points={},
)
