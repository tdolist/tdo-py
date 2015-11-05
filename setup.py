#!/usr/bin/env python3
from setuptools import setup, find_packages
import sys
import os


version = sys.version_info[:2]
if version < (3, 4):
    print('tdo requires Python version 3.4 or later' +
          ' ({}.{} detected).'.format(*version))
    sys.exit(-1)

VERSION = 'none'


setup(name='tdo',
      version=VERSION,
      description="A todo list tool for the terminal.",
      author='Felix Wittwer',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      entry_points={'console_scripts': [
          'tdo = tdo.main:main']})
