#!/usr/bin/env python3
"""
ScopeSim: A python package to simulate telescope observations
"""

from datetime import datetime
from distutils.core import setup
from setuptools import find_packages
# not needed, but stops setup being included by sphinx.apidoc
import pytest

# Version number
MAJOR = 0
MINOR = 1
ATTR = 'dev0'

VERSION = '%d.%d%s' % (MAJOR, MINOR, ATTR)


def write_version_py(filename='scopesim/version.py'):
    """Write a file version.py"""
    cnt = """
# THIS FILE GENERATED BY SCOPESIM SETUP.PY
version = '{}'
date    = '{}'
"""
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %T GMT')
    with open(filename, 'w') as fd:
        fd.write(cnt.format(VERSION, timestamp))


def setup_package():
    # Rewrite the version file every time
    # write_version_py()

    setup(name='ScopeSim',
          version=VERSION,
          description="Telescope observation simulator",
          author="Kieran Leschinski",
          author_email="kieran.leschinski@unive.ac.at",
          url="https://github.com/astronomyk/ScopeSim",
          package_dir={'scopesim': 'scopesim'},
          packages=find_packages(),
          include_package_data=True,
          install_requires=["numpy>=1.13",
                            "scipy>0.17",
                            "astropy>1.1.2",
                            "requests>2.0",
                            "synphot>0.1",
                            "matplotlib>1.5.0",
                            "pyyaml>3",
                            "beautifulsoup4"],
          classifiers=["Programming Language :: Python :: 3",
                       "License :: OSI Approved :: MIT License",
                       "Operating System :: OS Independent",
                       "Intended Audience :: Science/Research",
                       "Topic :: Scientific/Engineering :: Astronomy", ]
          )


if __name__ == '__main__':
    setup_package()
