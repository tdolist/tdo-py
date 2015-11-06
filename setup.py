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

VERSION = '0.5'


def install(mute=True):
    if not mute:
        print('Install tdo...')
    with open(os.devnull, 'w') as devnull:
        sys.stdout = devnull
        sys.stderr = devnull
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
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
    cleanup(filelist)
    if not mute:
        print('''Done. You can use it with \'tdo\'
For a list of available commands use \'tdo help\'''')


def uninstall():
    print('Uninstall tdo...')
    subprocess.call(['python3', sys.argv[0], 'install', '--record', 'files.txt'])
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
    print('Done.')


def cleanup(filelist):
    for entry in filelist:
        subprocess.call(['rm', '-rf', entry])


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'uninstall':
            uninstall()
        elif sys.argv[1] == 'install':
            if len(sys.argv) == 2:
                install(mute=False)
            else:
                install()
    else:
        command = ''
        if len(sys.argv) > 1:
            command = 'command \'{command}\' \
not supported\n'.format(command=sys.argv[1])
        print('''{command}usage: setup.py install
   or: setup.py uninstall'''.format(command=command))
