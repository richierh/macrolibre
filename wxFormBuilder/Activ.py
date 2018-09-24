#!usr/bin/env python
import os
import sys

path = "{}{}".format(os.getcwd(),"/Apps")
sys.path.append(path)
sys.path
os.getcwd()
cd = "{}{}".format(os.getcwd(),"/Apps")
os.chdir(cd)

from main import run

Run = run(None)
