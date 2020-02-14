#!/usr/bin/python
#
#

# coding=utf-8
from setuptools import setup, find_packages

setup(
    name='sdusbctl',
    version='1.0.0',
    description='SDU Sanbox Control API',
    long_description=
    ('Official API for SDU Sandbox control, accessible using a command line '
     'tool implemented in Python. Beta release - SDU reserves the right to '
     'modify the API functionality currently offered.'),
    author='SDU',
    author_email='support@shell-sdu.com',
    url='https://github.com/keshava/sdusbctl',
    keywords=['SDU Sandbox', 'API'],
    entry_points={'console_scripts': ['sdusbctl = sdusbstl.cli:main']},
    install_requires=[
        # Restriction that urllib3's version is less than 1.25 needed to avoid
        # requests dependency problem.
        'urllib3 >= 1.21.1, < 1.25',
        'six >= 1.10',
        'certifi',
        'python-dateutil',
        'requests',
        'tqdm',
        'python-slugify'
    ],
    packages=find_packages(),
    license='Shell-SDU 2.0')
