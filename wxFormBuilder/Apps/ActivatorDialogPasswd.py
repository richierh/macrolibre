"""Subclass of DialogPasswd, which is generated by wxFormBuilder."""

import wx
import Activator

# Implementing DialogPasswd
class ActivatorDialogPasswd( Activator.DialogPasswd ):
	def __init__( self, parent ):
		Activator.DialogPasswd.__init__( self, parent )

	# Handlers for DialogPasswd events.
	def btn_passwd( self, event ):
		# TODO: Implement btn_passwd
		print ("passwd")
		self.act = Activator.IntiWindow(self)
		self.txtctrl = self.m_textCtrl1
		
		self.passwd = self.txtctrl.GetValue()
		print (self.passwd)		
		if self.passwd == "admin" :
			print ("default")
			

		else :
			print ("keluar")
			self.Close()

