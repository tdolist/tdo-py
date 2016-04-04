#!/usr/bin/env python3
from setuptools import setup, find_packages
import sys


version = sys.version_info[:2]
if version < (3, 4):
    print('tdo requires Python version 3.4 or later' +
          ' ({}.{} detected).'.format(*version))
    sys.exit(-1)

VERSION = '1.1.2'


setup(name='tdo',
      version=VERSION,
      description="A todo list tool for the terminal.",
      author='tdolist',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      entry_points={'console_scripts': [
                  'tdo = tdo.main:main']})
