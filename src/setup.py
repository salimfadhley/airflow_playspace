#! /usr/bin/env python
from setuptools import setup
import os

PROJECT_ROOT, _ = os.path.split(__file__)
REVISION = '0.0.0'
PROJECT_NAME = 'airflow_playspace'
PROJECT_AUTHORS = "Salim Fadhley"
PROJECT_EMAILS = 'salimfadhley@gmail.com'
PROJECT_URL = "https://github.com/salimfadhley/airflow_playspace"
SHORT_DESCRIPTION = 'Demonstration'

try:
    DESCRIPTION = open(os.path.join(PROJECT_ROOT, "readme.md")).read()
except IOError:
    DESCRIPTION = SHORT_DESCRIPTION

try:
    REQUIREMENTS = list(open("requirements.txt").read().splitlines())
except IOError:
    REQUIREMENTS = []

setup(
    name=PROJECT_NAME.lower(),
    version=REVISION,
    author=PROJECT_AUTHORS,
    author_email=PROJECT_EMAILS,
    packages=['salair'],
    package_dir={"":"main"},
    zip_safe=True,
    include_package_data=False,
    install_requires=REQUIREMENTS,
    url=PROJECT_URL,
    description=SHORT_DESCRIPTION,
    long_description=DESCRIPTION,
    license='MIT',
    entry_points={
        'console_scripts': [
            'flash = blink1.flash:flash',
            'shine = blink1.shine:shine'
        ]
    }
)