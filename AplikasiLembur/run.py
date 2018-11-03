'''
Created on Nov 2, 2018

@author: binakarir
'''

import os
import sys
from MPython.main import Run


path = "{}{}".format(os.getcwd(),"/AppsSDS")
sys.path.append(path)
sys.path
os.getcwd()
cd = "{}{}".format(os.getcwd(),"/AppsSDS")
os.chdir(cd)


if __name__ == '__main__':
    pass

    Runapps = Run(None)
