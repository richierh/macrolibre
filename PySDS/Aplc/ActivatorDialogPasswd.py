"""Subclass of DialogPasswd, which is generated by wxFormBuilder."""

import Aplc.Activator as Activator


# Implementing DialogPasswd
class ActivatorDialogPasswd(Activator.DialogPasswd):

	def __init__(self, parent):
		Activator.DialogPasswd.__init__(self, parent)

	# Handlers for DialogPasswd events.
	def btn_passwd(self, event):
		# TODO: Implement btn_passwd
		from Aplc.aktifread import csvfile
		self.read = csvfile()
		passwd = self.read.read()
		print ("passwd")
		self.act = Activator.IntiWindow(self)
		self.txtctrl = self.m_textCtrl1
		
		self.passwd = self.txtctrl.GetValue()
		print (self.passwd)		
		if self.passwd == passwd :
			print ("default")
			from Aplc.ActivatorKonfigurasi import ActivatorKonfigurasi as ac
			self.opendialog = ac(self)
			self.opendialog.Show()
			self.Close()

		else :
			print ("keluar")
			self.Close()
