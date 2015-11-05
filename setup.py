#!/usr/bin/env python3
from setuptools import setup, find_packages
import sys
import os
import subprocess


version = sys.version_info[:2]
if version < (3, 4):
    print('tdo requires Python version 3.4 or later' +
          ' ({}.{} detected).'.format(*version))
    sys.exit(-1)

VERSION = 'none'


def install():
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
    filelist = ['{dir}/build'.format(dir=os.getcwd()),
                '{dir}/dist'.format(dir=os.getcwd()),
                '{dir}/tdo.egg-info'.format(dir=os.getcwd())]

    cleanup(filelist)


def uninstall():
    subprocess.call([sys.argv[0], 'install', '--record', 'files.txt'])
    filelist = []
    with open('files.txt') as files:
        filelist = files.readlines()
    for element in range(len(filelist)):
        filelist[element] = filelist[element][:-1]
    filelist.append('{dir}/.tdo'.format(dir=os.environ['HOME']))
    filelist.append('{dir}/build'.format(dir=os.getcwd()))
    filelist.append('{dir}/dist'.format(dir=os.getcwd()))
    filelist.append('{dir}/tdo.egg-info'.format(dir=os.getcwd()))
    filelist.append('{dir}/files.txt'.format(dir=os.getcwd()))

    cleanup(filelist)


def cleanup(filelist):
    for entry in filelist:
        subprocess.call(['rm', '-rf', entry])


if __name__ == '__main__':
    if sys.argv[1] == 'uninstall':
        uninstall()
    else:
        install()
