#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import sys

from setuptools import setup, find_packages

import gbif


install_requires = ['restkit']
long_description = codecs.open('README.md', "r", "utf-8").read()

setup(
    name='gbif',
    version=gbif.__version__,
    description=gbif.__doc__,
    long_description=long_description,
    author=gbif.__author__,
    author_email=gbif.__contact__,
    url=gbif.__homepage__,
    license='',
    keywords="gbif taxon taxonomy api bio",
    platforms=["any"],
    packages=find_packages(exclude=['tests']),
    install_requires=install_requires,
    zip_safe=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
    ]
)
