"""Subclass of WindowUtama, which is generated by wxFormBuilder."""

import wx
import AppsSDS.sds as sds
import AppsSDS.db.db as connectdb

connectdb.createdatabasename()


# Implementing WindowUtama
class SDSHollandWindowUtama(sds.WindowUtama):
	"""ljsdfalsdf"""
	
	def __init__(self, parent):
		sds.WindowUtama.__init__(self, parent)

	# Handlers for WindowUtama events.
	def btn_Close(self, event):
		# TODO: Implement btn_Close
	
		print ("Tutup Aplikasi")
		self.Close(True)
		pass

	def btn_selanjutnya(self, event):
	
		# TODO: Implement btn_gotopage2
		# from SDSHollandPage3 import SDSHollandPage3
		# SDSHollandPage2(self)
		
		for i in range(0, 3):
			print (i)

		self.m_panel101.Hide()
		self.m_panel6.Hide()
		self.m_panel2.Show()
		self.m_button1.Enable()
		self.m_button3.Enable()
		
		# SDSHollandPage3(self)
		self.Layout()

		pass

	def m_btn_tutupaplikasi(self, event):
		
		# dlg = wx.MessageDialog(self,"title","Apakah anda ingin menyimpan",\
		# 					style=wx.OK|wx.CANCEL)
		# dlg.SetOKCancelLabels("iya", "tidak")
		# val = dlg.ShowModal()
		import AppsSDS.messagebox as msgdlg
		self.getid = msgdlg.MessBx(None, "", style=wx.OK | wx.CANCEL)
		val = self.getid.getiddestroy()
		# print (getid.getiddestroy())
		if val == wx.ID_OK:
			print ("okay")
			self.Close()
			
		elif val == wx.ID_CANCEL:
			"""Membatalkan cancel"""
			pass
		
	def btn_balik(self, event):
		
		pass
	
	def m_btn_ttgaplikasi(self, event):
		pass
	
	def btnradio_formseleksi(self, event):
		print ("hello")
		self.m_panel7.Hide()
		self.m_panel8.Show()
		self.Layout()
		pass
		
	def btnradio_formtes(self, event):
		print ("I am over here")
		self.m_panel7.Show()
		self.m_panel8.Hide()
		self.Layout()
		pass

