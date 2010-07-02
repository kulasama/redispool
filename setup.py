#!/usr/bin/env python

from distutils.extension import Extension
from setuptools import setup, find_packages
from distutils.core import setup, Extension
import sys


setup(
    name = "redispool",
    version = "0.0.1",
    packages = ['redispool',],
    package_dir = {'redispool':'src',},   # tell distutils packages are under src
    license = "Apache 2.0",
    author = "kula",
    author_email = "kulasama@gmail.com",
    zip_safe = False,
)
