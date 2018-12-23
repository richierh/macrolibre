#!usr/bin/env python
"""
from oscheck import *
import wx
"""

import os
import sys

path = "{}{}".format(os.getcwd(), "/AppsSDS")
sys.path.append(path)
sys.path
# print (sys.path)
os.getcwd()
cd = "{}{}".format(os.getcwd(), "/AppsSDS")
os.chdir(cd)

import AppsSDS.main as run

# runapps = run.run(None)
#import run


# Runapps = run(None)
# menjalankan aplikasi
