#!usr/bin/env python
import os
import sys
from oscheck import *
import wx

path = "{}{}".format(os.getcwd(),"/AppsSDS")
sys.path.append(path)
sys.path
os.getcwd()
cd = "{}{}".format(os.getcwd(),"/AppsSDS")
os.chdir(cd)

from main import run


#menjalankan aplikasi