#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='jetstream.cli',
    version='0.1.0',
    description='Command-line interface for the Jetstream framework',
    long_description=readme + '\n\n' + history,
    author='Petri Savolainen',
    author_email='petri.savolainen@koodaamo.fi',
    url='https://github.com/petri/jetstream.cli',
    namespace_packages=['jetstream'],
    packages = ['jetstream.cli'],
    include_package_data=True,
    install_requires=[
        "setuptools",
        "docopt",
    ],
    entry_points={
        'console_scripts': [
            'jet = jetstream.cli.jet:main',
        ],
    },
    license="BSD",
    zip_safe=False,
    keywords='jetstream.cli',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests.test_suite',
)
