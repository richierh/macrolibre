#!usr/bin/env python
import wx

class main(wx.Frame):
	def __init__(self,*args,**kwrgs):
		super(main,self).__init__(*args,**kwrgs)
		self.Maximize(True)

class mainpanel(wx.Frame):
	def __init__(self,*args,**kwrgs):
		super(main,self).__init__(*args,**kwrgs)
		self.Enable(False)


if __name__=="__main__":
	root = wx.App()
	s = main(None).Show(True)
	root.MainLoop()

