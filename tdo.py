#!/usr/bin/env python3
import tdo
import os
import sys


def run():
    path = sys.argv[0].rsplit('/', 1)[0]
    os.chdir('{path}/tdo'.format(path=path))
    tdo.main()


if __name__ == '__main__':
    run()
