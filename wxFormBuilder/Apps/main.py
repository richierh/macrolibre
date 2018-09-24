#!usr/bin/env python


import wx
from ActivatorIntiWindow import ActivatorIntiWindow as I
from ActivatorDialogPasswd import ActivatorDialogPasswd as D


class run(I,D):
	def __init__(self,*args,**kwrgs):
		super(run,self).__init__(*args,**kwrgs)
	pass

root = wx.App()
start = run(None)
start.Show()
root.MainLoop()	
if __name__=="__main__":
	root = wx.App()
	start = run(None)
	start.Show()
	root.MainLoop()	