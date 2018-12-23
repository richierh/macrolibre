"""Subclass of Konfigurasi, which is generated by wxFormBuilder."""

import Aplc.Activator as Activator
from _datetime import datetime
import wx
from Aplc.aktifread import FileDate


# Implementing Konfigurasi
class ActivatorKonfigurasi(Activator.Konfigurasi):

	def __init__(self, parent):
		Activator.Konfigurasi.__init__(self, parent)
		self.m_sdbSizer1OK.SetLabel("Simpan")
		self.m_sdbSizer1Cancel.SetLabel("Batal")
		
		
		self.WindowUtama = parent
# 		Ini adalah kondisi untuk melihat apakah sudah menyimpan 
# 		tanggal apa belum ?
		self.kondisiwaktu = FileDate()
		self.x,self.y=self.kondisiwaktu.check_date()
		self.passwd,self.p =self.kondisiwaktu.check_password()
		print (self.x,self.y)
		
	
		if self.y == "ada":
			self.tanggal_aktif.SetLabel(self.x[0])
	
			print ("filenya ada")
		else :
			print ("file tidak ada")
			self.tanggal_aktif.SetLabel("Belum diset")
			
		if self.p == "ada":
			self.password.SetLabel(self.passwd[0])
			print ("filenya ada")
		else :
			print ("file tidak ada")
			self.password.SetLabel("")


		self.Layout()
	
	def m_datechange(self, event):
		self.date = self.m_datePicker1.GetValue()
		self.setdatekonf = self.date.Format("%d/%m/%y")
		
		print ("{}".format(self.setdatekonf))
		self.tanggal_aktif.SetLabel(self.setdatekonf)
		self.Layout()
		
		
		pass
		
		

	# Handlers for Konfigurasi events.
	def btn_lanjut(self, event):
		# TODO: Implement btn_lanjut
		self.WindowUtama.root.Show()
		self.Close()

		pass

	def btn_cancel(self, event):
		# TODO: Implement btn_cancel
		self.WindowUtama.root.Show()
		self.Close()
		
		pass
	
	def btn_aktifkan(self, event):
# 		Merupakan fungsi untuk mengaktifkan settingan 
		
		pass

	def btn_non_aktifkan(self, event):
		self.tanggal_aktif.SetLabel("NonAktif")
		
		pass
	
	def btn_ubah(self, event):
		self.password.SetLabel(self.ubah_password.GetValue())
		self.Layout()
		pass


if __name__=="__main__":
	root=wx.App()
	run=ActivatorKonfigurasi(None)
	run.Show()
	root.MainLoop()