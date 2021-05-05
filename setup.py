#!/usr/bin/env python
# -*- coding: utf-8 -*-
from codecs import open
from os.path import (abspath, dirname, join)
from subprocess import call

from setuptools import (Command, find_packages, setup)

from package_name.version import *

this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


class RunTests(Command):
    """Run all tests."""

    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        err_no = call(['py.test', '--cov=package_name', '--cov-report=term-missing'])
        raise SystemExit(err_no)


setup(
    name='package_name',
    version=__version__,
    description='A Short Description of the Package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/thedeltaflyer/python_lib_with_cli',
    author=__maintainer__,
    author_email=__email__,
    license=__license__,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='keywords that describe project',
    project_urls={
        'Source': 'https://github.com/thedeltaflyer/python_lib_with_cli',
        'Tracker': 'https://github.com/thedeltaflyer/python_lib_with_cli/issues',
    },
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=[
        'requests>=2.25,<3'
    ],
    python_requires='~=3.9',
    extras_require={
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points={
        'console_scripts': [
            'package_cli=package_name.cli:main',
        ],
    },
    cmdclass={'test': RunTests},
)
