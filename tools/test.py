# -*- coding: utf-8 -*-

import sys
import os
import subprocess

cwd = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, cwd)

if __name__ == '__main__':
    if (os.getcwd() != cwd):
        os.chdir(cwd)
    os.putenv("PYTHONPATH", ';'.join(str(i) for i in sys.path))
    subprocess.call(['py.test', '-s', 'tests'], shell= True)
