'''
Created on Nov 2, 2018

@author: binakarir
'''

import os
import sys
from MPython.app import MyApp


path = "{}{}".format(os.getcwd(),"/MPython")
sys.path.append(path)
sys.path
os.getcwd()
cd = "{}{}".format(os.getcwd(),"/MPython")
os.chdir(cd)


if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
