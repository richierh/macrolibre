# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 29 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

from AppsSDS.SDSHollandPage2 import Page2
from AppsSDS.style import main
import wx
import wx.xrc
import wx.adv
import wx.grid

###########################################################################
## Class WindowUtama
###########################################################################

class WindowUtama ( main ):

	def __init__( self, parent ):
		main.__init__ ( self, parent, id = wx.ID_ANY, title = u"BINAKARIR", pos = wx.DefaultPosition, size = wx.Size( 1000,1000 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer101 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel101 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer13 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer13.SetFlexibleDirection( wx.BOTH )
		fgSizer13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_radioBtn1 = wx.RadioButton( self.m_panel101, wx.ID_ANY, u"Form Seleksi", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer13.Add( self.m_radioBtn1, 0, wx.ALL, 5 )

		self.m_radioBtn2 = wx.RadioButton( self.m_panel101, wx.ID_ANY, u"Form Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer13.Add( self.m_radioBtn2, 0, wx.ALL, 5 )


		self.m_panel101.SetSizer( fgSizer13 )
		self.m_panel101.Layout()
		fgSizer13.Fit( self.m_panel101 )
		bSizer101.Add( self.m_panel101, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.halaman1 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.halaman1.SetBackgroundColour( wx.Colour( 174, 243, 171 ) )

		fgSizer14 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer14.AddGrowableCol( 0 )
		fgSizer14.AddGrowableCol( 1 )
		fgSizer14.AddGrowableCol( 2 )
		fgSizer14.AddGrowableRow( 0 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_panel7 = wx.Panel( self.halaman1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer4 = wx.FlexGridSizer( 10, 2, 0, 0 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.no_tes = wx.StaticText( self.m_panel7, wx.ID_ANY, u"No Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.no_tes.Wrap( -1 )

		fgSizer4.Add( self.no_tes, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.no_tes_input = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer4.Add( self.no_tes_input, 0, wx.ALL|wx.EXPAND, 5 )

		self.tanggal_tes = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Tanggal Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tanggal_tes.Wrap( -1 )

		fgSizer4.Add( self.tanggal_tes, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tanggal_tes_input = wx.adv.DatePickerCtrl( self.m_panel7, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 200,-1 ), wx.adv.DP_DEFAULT )
		fgSizer4.Add( self.tanggal_tes_input, 0, wx.ALL, 5 )

		self.nama_kandidat = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Nama Kandidat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nama_kandidat.Wrap( -1 )

		fgSizer4.Add( self.nama_kandidat, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.nama_kandidat_input = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		fgSizer4.Add( self.nama_kandidat_input, 0, wx.ALL|wx.EXPAND, 5 )

		self.jenis_kelamin = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jenis_kelamin.Wrap( -1 )

		fgSizer4.Add( self.jenis_kelamin, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		jenis_kelamin_inputChoices = [ u"Laki-Laki", u"Perempuan" ]
		self.jenis_kelamin_input = wx.Choice( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, jenis_kelamin_inputChoices, 0 )
		self.jenis_kelamin_input.SetSelection( 1 )
		fgSizer4.Add( self.jenis_kelamin_input, 0, wx.ALL, 5 )

		self.tanggal_lahir = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tanggal_lahir.Wrap( -1 )

		fgSizer4.Add( self.tanggal_lahir, 0, wx.ALL, 5 )

		self.tanggal_lahir_input = wx.adv.DatePickerCtrl( self.m_panel7, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 200,-1 ), wx.adv.DP_DEFAULT )
		fgSizer4.Add( self.tanggal_lahir_input, 0, wx.ALL, 5 )

		self.pendidikan_terakhir = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Pendidikan Terakhir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pendidikan_terakhir.Wrap( -1 )

		fgSizer4.Add( self.pendidikan_terakhir, 0, wx.ALL, 5 )

		pendidikan_terakhir_inputChoices = [ u"SD", u"SMP", u"SMA/Sederajat", u"S1", u"S2", u"S3" ]
		self.pendidikan_terakhir_input = wx.Choice( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pendidikan_terakhir_inputChoices, 0 )
		self.pendidikan_terakhir_input.SetSelection( 2 )
		fgSizer4.Add( self.pendidikan_terakhir_input, 0, wx.ALL, 5 )

		self.jurusan = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Jurusan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jurusan.Wrap( -1 )

		fgSizer4.Add( self.jurusan, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.jurusan_input = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.jurusan_input, 0, wx.ALL|wx.EXPAND, 5 )

		self.kota = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Kota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kota.Wrap( -1 )

		fgSizer4.Add( self.kota, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.kota_input = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.kota_input, 0, wx.ALL|wx.EXPAND, 5 )

		self.perusahaan_instansi = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Perusahaan/Instansi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.perusahaan_instansi.Wrap( -1 )

		fgSizer4.Add( self.perusahaan_instansi, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.perusahaan_instansi_input = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.perusahaan_instansi_input, 0, wx.ALL|wx.EXPAND, 5 )

		self.posisi_jabatan = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Posisi/Jabatan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.posisi_jabatan.Wrap( -1 )

		fgSizer4.Add( self.posisi_jabatan, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.posisi_jabatan_input = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.posisi_jabatan_input, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel7.SetSizer( fgSizer4 )
		self.m_panel7.Layout()
		fgSizer4.Fit( self.m_panel7 )
		fgSizer14.Add( self.m_panel7, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_panel8 = wx.Panel( self.halaman1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel8.Hide()

		fgSizer15 = wx.FlexGridSizer( 13, 2, 0, 1 )
		fgSizer15.SetFlexibleDirection( wx.BOTH )
		fgSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.nama2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nama2.Wrap( -1 )

		fgSizer15.Add( self.nama2, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.no_tes_input2 = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		fgSizer15.Add( self.no_tes_input2, 0, wx.ALL, 5 )

		self.tanggal_tes2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Tanggal Tes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tanggal_tes2.Wrap( -1 )

		fgSizer15.Add( self.tanggal_tes2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tanggal_tes_input2 = wx.adv.DatePickerCtrl( self.m_panel8, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 200,-1 ), wx.adv.DP_DEFAULT )
		fgSizer15.Add( self.tanggal_tes_input2, 0, wx.ALL, 5 )

		self.jenis_kelamin2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Jenis Kelamin", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jenis_kelamin2.Wrap( -1 )

		fgSizer15.Add( self.jenis_kelamin2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		jenis_kelamin_input2Choices = [ u"Laki-Laki", u"Perempuan" ]
		self.jenis_kelamin_input2 = wx.Choice( self.m_panel8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, jenis_kelamin_input2Choices, 0 )
		self.jenis_kelamin_input2.SetSelection( 1 )
		fgSizer15.Add( self.jenis_kelamin_input2, 0, wx.ALL, 5 )

		self.tanggal_lahir2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Tanggal Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tanggal_lahir2.Wrap( -1 )

		fgSizer15.Add( self.tanggal_lahir2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.tanggal_lahir_input2 = wx.adv.DatePickerCtrl( self.m_panel8, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 200,-1 ), wx.adv.DP_DEFAULT )
		fgSizer15.Add( self.tanggal_lahir_input2, 0, wx.ALL, 5 )

		self.asal_sekolah2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Asal Sekolah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.asal_sekolah2.Wrap( -1 )

		fgSizer15.Add( self.asal_sekolah2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.asal_sekolah_input2 = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer15.Add( self.asal_sekolah_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.jurusan2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Jurusan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jurusan2.Wrap( -1 )

		fgSizer15.Add( self.jurusan2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.jurusan_input2 = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer15.Add( self.jurusan_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.asal_universitas2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Asal Universitas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.asal_universitas2.Wrap( -1 )

		fgSizer15.Add( self.asal_universitas2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.asal_universitas_input2 = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer15.Add( self.asal_universitas_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.jurusan2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Jurusan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.jurusan2.Wrap( -1 )

		fgSizer15.Add( self.jurusan2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.jurusan_input2 = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer15.Add( self.jurusan_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.kota2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Kota", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kota2.Wrap( -1 )

		fgSizer15.Add( self.kota2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.kota_input2 = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer15.Add( self.kota_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.hobi2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Hobi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.hobi2.Wrap( -1 )

		fgSizer15.Add( self.hobi2, 0, wx.ALL, 5 )

		self.hobi_input2 = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		fgSizer15.Add( self.hobi_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.prestasi_akademik2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Prestasi Akademik", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.prestasi_akademik2.Wrap( -1 )

		fgSizer15.Add( self.prestasi_akademik2, 0, wx.ALL, 5 )

		self.prestasi_akademik_input2 = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		fgSizer15.Add( self.prestasi_akademik_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.prestasi_non_akademik2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Prestasi Non Akademik", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.prestasi_non_akademik2.Wrap( -1 )

		fgSizer15.Add( self.prestasi_non_akademik2, 0, wx.ALL, 5 )

		self.prestasi_non_akademik_input2 = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		fgSizer15.Add( self.prestasi_non_akademik_input2, 0, wx.ALL|wx.EXPAND, 5 )

		self.ekskul_yang_diikuti2 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Ekskul Yang Diikuti", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ekskul_yang_diikuti2.Wrap( -1 )

		fgSizer15.Add( self.ekskul_yang_diikuti2, 0, wx.ALL, 5 )

		self.ekskul_yang_diikuti_input2 = wx.TextCtrl( self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		fgSizer15.Add( self.ekskul_yang_diikuti_input2, 0, wx.ALL|wx.EXPAND, 5 )


		self.m_panel8.SetSizer( fgSizer15 )
		self.m_panel8.Layout()
		fgSizer15.Fit( self.m_panel8 )
		fgSizer14.Add( self.m_panel8, 1, wx.ALL|wx.EXPAND, 5 )

		self.m_panel21 = wx.Panel( self.halaman1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel21.SetBackgroundColour( wx.Colour( 174, 243, 171 ) )

		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_bitmap3 = wx.StaticBitmap( self.m_panel21, wx.ID_ANY, wx.Bitmap( u"images/binakarir.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.m_bitmap3, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.m_panel21.SetSizer( bSizer25 )
		self.m_panel21.Layout()
		bSizer25.Fit( self.m_panel21 )
		fgSizer14.Add( self.m_panel21, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )


		self.halaman1.SetSizer( fgSizer14 )
		self.halaman1.Layout()
		fgSizer14.Fit( self.halaman1 )
		bSizer101.Add( self.halaman1, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.m_panel9 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button3 = wx.Button( self.m_panel9, wx.ID_ANY, u"Ke Awal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button3.Enable( False )

		bSizer5.Add( self.m_button3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


		bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self.m_panel9, wx.ID_ANY, u"<Page Sebelumnya", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button1.Enable( False )

		bSizer5.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.m_button2 = wx.Button( self.m_panel9, wx.ID_ANY, u">Page Selanjutnya", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


		self.m_panel9.SetSizer( bSizer5 )
		self.m_panel9.Layout()
		bSizer5.Fit( self.m_panel9 )
		bSizer101.Add( self.m_panel9, 0, wx.ALL|wx.EXPAND, 5 )

		self.halaman2 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.halaman2.Hide()

		bSizer301 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow6 = wx.ScrolledWindow( self.halaman2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow6.SetScrollRate( 5, 5 )
		bSizer311 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel201 = Page2( self.m_scrolledWindow6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer311.Add( self.m_panel201, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_scrolledWindow6.SetSizer( bSizer311 )
		self.m_scrolledWindow6.Layout()
		bSizer311.Fit( self.m_scrolledWindow6 )
		bSizer301.Add( self.m_scrolledWindow6, 1, wx.EXPAND |wx.ALL, 5 )


		self.halaman2.SetSizer( bSizer301 )
		self.halaman2.Layout()
		bSizer301.Fit( self.halaman2 )
		bSizer101.Add( self.halaman2, 5, wx.ALL|wx.EXPAND, 5 )

		self.halaman3 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.halaman3.Hide()

		bSizer15 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow1 = wx.ScrolledWindow( self.halaman3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel61 = Page3( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer16.Add( self.m_panel61, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_scrolledWindow1.SetSizer( bSizer16 )
		self.m_scrolledWindow1.Layout()
		bSizer16.Fit( self.m_scrolledWindow1 )
		bSizer15.Add( self.m_scrolledWindow1, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		self.halaman3.SetSizer( bSizer15 )
		self.halaman3.Layout()
		bSizer15.Fit( self.halaman3 )
		bSizer101.Add( self.halaman3, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		self.halaman4 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.halaman4.Hide()

		bSizer151 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow11 = wx.ScrolledWindow( self.halaman4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow11.SetScrollRate( 5, 5 )
		bSizer161 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel611 = Page4( self.m_scrolledWindow11, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer161.Add( self.m_panel611, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_scrolledWindow11.SetSizer( bSizer161 )
		self.m_scrolledWindow11.Layout()
		bSizer161.Fit( self.m_scrolledWindow11 )
		bSizer151.Add( self.m_scrolledWindow11, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		self.halaman4.SetSizer( bSizer151 )
		self.halaman4.Layout()
		bSizer151.Fit( self.halaman4 )
		bSizer101.Add( self.halaman4, 1, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.halaman5 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.halaman5.Hide()

		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow7 = wx.ScrolledWindow( self.halaman5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow7.SetScrollRate( 5, 5 )
		bSizer29 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel18 = Page5( self.m_scrolledWindow7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer29.Add( self.m_panel18, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_scrolledWindow7.SetSizer( bSizer29 )
		self.m_scrolledWindow7.Layout()
		bSizer29.Fit( self.m_scrolledWindow7 )
		bSizer27.Add( self.m_scrolledWindow7, 1, wx.EXPAND |wx.ALL, 5 )


		self.halaman5.SetSizer( bSizer27 )
		self.halaman5.Layout()
		bSizer27.Fit( self.halaman5 )
		bSizer101.Add( self.halaman5, 1, wx.EXPAND |wx.ALL, 5 )

		self.halaman6 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.halaman6.Hide()

		bSizer30 = wx.BoxSizer( wx.VERTICAL )

		self.m_scrolledWindow8 = wx.ScrolledWindow( self.halaman6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow8.SetScrollRate( 5, 5 )
		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel20 = Page6( self.m_scrolledWindow8, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer31.Add( self.m_panel20, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_scrolledWindow8.SetSizer( bSizer31 )
		self.m_scrolledWindow8.Layout()
		bSizer31.Fit( self.m_scrolledWindow8 )
		bSizer30.Add( self.m_scrolledWindow8, 1, wx.EXPAND |wx.ALL, 5 )


		self.halaman6.SetSizer( bSizer30 )
		self.halaman6.Layout()
		bSizer30.Fit( self.halaman6 )
		bSizer101.Add( self.halaman6, 1, wx.EXPAND |wx.ALL, 5 )


		self.m_panel1.SetSizer( bSizer101 )
		self.m_panel1.Layout()
		bSizer101.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu2 = wx.Menu()
		self.m_menuItem3 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Database", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem3 )

		self.m_menuItem2 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Tutup Aplikasi", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem2 )

		self.m_menubar1.Append( self.m_menu2, u"Berkas" )

		self.m_menu21 = wx.Menu()
		self.m_menuItem31 = wx.MenuItem( self.m_menu21, wx.ID_ANY, u"Tentang Aplikasi", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu21.Append( self.m_menuItem31 )

		self.m_menubar1.Append( self.m_menu21, u"Tentang" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_radioBtn1.Bind( wx.EVT_RADIOBUTTON, self.btnradio_formtes )
		self.m_radioBtn2.Bind( wx.EVT_RADIOBUTTON, self.btnradio_formseleksi )
		self.no_tes_input.Bind( wx.EVT_TEXT, self.no_tes_inputOnText )
		self.m_button3.Bind( wx.EVT_BUTTON, self.btn_kembaliawal )
		self.m_button1.Bind( wx.EVT_BUTTON, self.btn_balik )
		self.m_button2.Bind( wx.EVT_BUTTON, self.btn_selanjutnya )
		self.Bind( wx.EVT_MENU, self.m_btn_tutupaplikasi, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.m_btn_ttgaplikasi, id = self.m_menuItem31.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnradio_formtes( self, event ):
		event.Skip()

	def btnradio_formseleksi( self, event ):
		event.Skip()

	def no_tes_inputOnText( self, event ):
		event.Skip()

	def btn_kembaliawal( self, event ):
		event.Skip()

	def btn_balik( self, event ):
		event.Skip()

	def btn_selanjutnya( self, event ):
		event.Skip()

	def m_btn_tutupaplikasi( self, event ):
		event.Skip()

	def m_btn_ttgaplikasi( self, event ):
		event.Skip()


###########################################################################
## Class MyPanel10
###########################################################################

class MyPanel10 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )


	def __del__( self ):
		pass


###########################################################################
## Class Page6
###########################################################################

class Page6 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer32 = wx.BoxSizer( wx.VERTICAL )


		self.SetSizer( bSizer32 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class Page5
###########################################################################

class Page5 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer15 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer15.SetFlexibleDirection( wx.BOTH )
		fgSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_button4 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer15.Add( self.m_button4, 0, wx.ALL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer15.Add( self.m_button5, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer15.Add( self.m_button6, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer15 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class Page2copy
###########################################################################

class Page2copy ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"OCCUPATIONAL DAYDREAM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer10.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		fgSizer71 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer71.AddGrowableCol( 1 )
		fgSizer71.SetFlexibleDirection( wx.BOTH )
		fgSizer71.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		fgSizer71.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		fgSizer71.Add( self.m_textCtrl7, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.openlistbox1 = wx.Button( self, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer71.Add( self.openlistbox1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.label_event = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.label_event.Wrap( -1 )

		fgSizer71.Add( self.label_event, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		fgSizer71.Add( self.m_staticText10, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		fgSizer71.Add( self.m_textCtrl6, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.openlistbox2 = wx.Button( self, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer71.Add( self.openlistbox2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText131 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText131.Wrap( -1 )

		fgSizer71.Add( self.m_staticText131, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText132 = wx.StaticText( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText132.Wrap( -1 )

		fgSizer71.Add( self.m_staticText132, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer71.Add( self.m_textCtrl21, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.openlistbox3 = wx.Button( self, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer71.Add( self.openlistbox3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText133 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText133.Wrap( -1 )

		fgSizer71.Add( self.m_staticText133, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText134 = wx.StaticText( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText134.Wrap( -1 )

		fgSizer71.Add( self.m_staticText134, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl20 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer71.Add( self.m_textCtrl20, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.openlistbox4 = wx.Button( self, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer71.Add( self.openlistbox4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText137 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText137.Wrap( -1 )

		fgSizer71.Add( self.m_staticText137, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText138 = wx.StaticText( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText138.Wrap( -1 )

		fgSizer71.Add( self.m_staticText138, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl19 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer71.Add( self.m_textCtrl19, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.openlistbox5 = wx.Button( self, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer71.Add( self.openlistbox5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText1381 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1381.Wrap( -1 )

		fgSizer71.Add( self.m_staticText1381, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText139 = wx.StaticText( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText139.Wrap( -1 )

		fgSizer71.Add( self.m_staticText139, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_textCtrl22 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer71.Add( self.m_textCtrl22, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.openlistbox6 = wx.Button( self, wx.ID_ANY, u"Cari", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer71.Add( self.openlistbox6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText140 = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText140.Wrap( -1 )

		fgSizer71.Add( self.m_staticText140, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer10.Add( fgSizer71, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer10 )
		self.Layout()

		# Connect Events
		self.openlistbox1.Bind( wx.EVT_BUTTON, self.openlistbox1OnButtonClick )
		self.openlistbox2.Bind( wx.EVT_BUTTON, self.openlistbox2OnButtonClick )
		self.openlistbox3.Bind( wx.EVT_BUTTON, self.openlistbox3OnButtonClick )
		self.openlistbox4.Bind( wx.EVT_BUTTON, self.openlistbox4OnButtonClick )
		self.openlistbox5.Bind( wx.EVT_BUTTON, self.openlistbox5OnButtonClick )
		self.openlistbox6.Bind( wx.EVT_BUTTON, self.openlistbox6OnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def openlistbox1OnButtonClick( self, event ):
		event.Skip()

	def openlistbox2OnButtonClick( self, event ):
		event.Skip()

	def openlistbox3OnButtonClick( self, event ):
		event.Skip()

	def openlistbox4OnButtonClick( self, event ):
		event.Skip()

	def openlistbox5OnButtonClick( self, event ):
		event.Skip()

	def openlistbox6OnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Page3
###########################################################################

class Page3 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 900,700 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"ACTIVITIES", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		bSizer16.Add( self.m_staticText24, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText25 = wx.StaticText( self, wx.ID_ANY, u"REALITY", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		bSizer9.Add( self.m_staticText25, 0, wx.ALL|wx.EXPAND, 5 )

		fgSizer9 = wx.FlexGridSizer( 15, 3, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer9.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"L", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		fgSizer9.Add( self.m_staticText28, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"D", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		fgSizer9.Add( self.m_staticText29, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"R1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.SetLabelMarkup( u"R1" )
		self.m_staticText14.Wrap( -1 )

		fgSizer9.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.m_checkBox21112 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox21112, 0, wx.ALL, 5 )

		self.m_checkBox211 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox211, 0, wx.ALL, 5 )

		self.m_staticText1411 = wx.StaticText( self, wx.ID_ANY, u"R2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1411.SetLabelMarkup( u"R2" )
		self.m_staticText1411.Wrap( -1 )

		fgSizer9.Add( self.m_staticText1411, 0, wx.ALL, 5 )

		self.m_checkBox210 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox210, 0, wx.ALL, 5 )

		self.m_checkBox29 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox29, 0, wx.ALL, 5 )

		self.m_staticText141 = wx.StaticText( self, wx.ID_ANY, u"R3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141.Wrap( -1 )

		fgSizer9.Add( self.m_staticText141, 0, wx.ALL, 5 )

		self.m_checkBox28 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox28, 0, wx.ALL, 5 )

		self.m_checkBox27 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox27, 0, wx.ALL, 5 )

		self.m_staticText1412 = wx.StaticText( self, wx.ID_ANY, u"R4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1412.Wrap( -1 )

		fgSizer9.Add( self.m_staticText1412, 0, wx.ALL, 5 )

		self.m_checkBox26 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox26, 0, wx.ALL, 5 )

		self.m_checkBox25 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox25, 0, wx.ALL, 5 )

		self.m_staticText14121 = wx.StaticText( self, wx.ID_ANY, u"R5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14121.Wrap( -1 )

		fgSizer9.Add( self.m_staticText14121, 0, wx.ALL, 5 )

		self.m_checkBox24 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox24, 0, wx.ALL, 5 )

		self.m_checkBox23 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox23, 0, wx.ALL, 5 )

		self.m_staticText14122 = wx.StaticText( self, wx.ID_ANY, u"R6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14122.Wrap( -1 )

		fgSizer9.Add( self.m_staticText14122, 0, wx.ALL, 5 )

		self.m_checkBox22 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox22, 0, wx.ALL, 5 )

		self.m_checkBox21 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox21, 0, wx.ALL, 5 )

		self.m_staticText14123 = wx.StaticText( self, wx.ID_ANY, u"R7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14123.Wrap( -1 )

		fgSizer9.Add( self.m_staticText14123, 0, wx.ALL, 5 )

		self.m_checkBox2 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox2, 0, wx.ALL, 5 )

		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox1, 0, wx.ALL, 5 )

		self.m_staticText141241 = wx.StaticText( self, wx.ID_ANY, u"R8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141241.Wrap( -1 )

		fgSizer9.Add( self.m_staticText141241, 0, wx.ALL, 5 )

		self.m_checkBox2112 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox2112, 0, wx.ALL, 5 )

		self.m_checkBox11 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox11, 0, wx.ALL, 5 )

		self.m_staticText14124 = wx.StaticText( self, wx.ID_ANY, u"R9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14124.Wrap( -1 )

		fgSizer9.Add( self.m_staticText14124, 0, wx.ALL, 5 )

		self.m_checkBox46 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox46, 0, wx.ALL, 5 )

		self.m_checkBox47 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox47, 0, wx.ALL, 5 )

		self.m_staticText49 = wx.StaticText( self, wx.ID_ANY, u"R10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )

		fgSizer9.Add( self.m_staticText49, 0, wx.ALL, 5 )

		self.m_checkBox471 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox471, 0, wx.ALL, 5 )

		self.m_checkBox472 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox472, 0, wx.ALL, 5 )

		self.m_staticText14125 = wx.StaticText( self, wx.ID_ANY, u"R11", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14125.Wrap( -1 )

		fgSizer9.Add( self.m_staticText14125, 0, wx.ALL, 5 )

		self.m_checkBox473 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox473, 0, wx.ALL, 5 )

		self.m_checkBox476 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox476, 0, wx.ALL, 5 )

		self.m_staticText14126 = wx.StaticText( self, wx.ID_ANY, u"R12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14126.Wrap( -1 )

		fgSizer9.Add( self.m_staticText14126, 0, wx.ALL, 5 )

		self.m_checkBox475 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox475, 0, wx.ALL, 5 )

		self.m_checkBox474 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox474, 0, wx.ALL, 5 )

		self.m_staticText14127 = wx.StaticText( self, wx.ID_ANY, u"R13", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14127.Wrap( -1 )

		fgSizer9.Add( self.m_staticText14127, 0, wx.ALL, 5 )

		self.m_checkBox4741 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox4741, 0, wx.ALL, 5 )

		self.m_checkBox4742 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox4742, 0, wx.ALL, 5 )

		self.m_staticText50 = wx.StaticText( self, wx.ID_ANY, u"R14", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )

		fgSizer9.Add( self.m_staticText50, 0, wx.ALL, 5 )

		self.m_checkBox4743 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox4743, 0, wx.ALL, 5 )

		self.m_checkBox4744 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer9.Add( self.m_checkBox4744, 0, wx.ALL, 5 )


		bSizer9.Add( fgSizer9, 1, wx.EXPAND, 5 )


		bSizer8.Add( bSizer9, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer91 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText251 = wx.StaticText( self, wx.ID_ANY, u"REALITY", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText251.Wrap( -1 )

		bSizer91.Add( self.m_staticText251, 0, wx.ALL|wx.EXPAND, 5 )

		fgSizer91 = wx.FlexGridSizer( 15, 3, 0, 0 )
		fgSizer91.SetFlexibleDirection( wx.BOTH )
		fgSizer91.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer91.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText281 = wx.StaticText( self, wx.ID_ANY, u"L", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText281.Wrap( -1 )

		fgSizer91.Add( self.m_staticText281, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText291 = wx.StaticText( self, wx.ID_ANY, u"D", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText291.Wrap( -1 )

		fgSizer91.Add( self.m_staticText291, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText142 = wx.StaticText( self, wx.ID_ANY, u"R1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText142.SetLabelMarkup( u"R1" )
		self.m_staticText142.Wrap( -1 )

		fgSizer91.Add( self.m_staticText142, 0, wx.ALL, 5 )

		self.m_checkBox211121 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TAB_TRAVERSAL )
		fgSizer91.Add( self.m_checkBox211121, 0, wx.ALL, 5 )

		self.m_checkBox2111 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TAB_TRAVERSAL )
		fgSizer91.Add( self.m_checkBox2111, 0, wx.ALL, 5 )

		self.m_staticText14111 = wx.StaticText( self, wx.ID_ANY, u"R2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14111.SetLabelMarkup( u"R2" )
		self.m_staticText14111.Wrap( -1 )

		fgSizer91.Add( self.m_staticText14111, 0, wx.ALL, 5 )

		self.m_checkBox2101 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TAB_TRAVERSAL )
		fgSizer91.Add( self.m_checkBox2101, 0, wx.ALL, 5 )

		self.m_checkBox291 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.TAB_TRAVERSAL )
		fgSizer91.Add( self.m_checkBox291, 0, wx.ALL, 5 )

		self.m_staticText1413 = wx.StaticText( self, wx.ID_ANY, u"R3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1413.Wrap( -1 )

		fgSizer91.Add( self.m_staticText1413, 0, wx.ALL, 5 )

		self.m_checkBox281 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_checkBox281, 0, wx.ALL, 5 )

		self.m_checkBox271 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_checkBox271, 0, wx.ALL, 5 )

		self.m_staticText14128 = wx.StaticText( self, wx.ID_ANY, u"R4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14128.Wrap( -1 )

		fgSizer91.Add( self.m_staticText14128, 0, wx.ALL, 5 )

		self.m_checkBox261 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_checkBox261, 0, wx.ALL, 5 )

		self.m_checkBox251 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_checkBox251, 0, wx.ALL, 5 )

		self.m_staticText141211 = wx.StaticText( self, wx.ID_ANY, u"R5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141211.Wrap( -1 )

		fgSizer91.Add( self.m_staticText141211, 0, wx.ALL, 5 )

		self.m_checkBox241 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_checkBox241, 0, wx.ALL, 5 )

		self.m_checkBox231 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_checkBox231, 0, wx.ALL, 5 )

		self.m_staticText141221 = wx.StaticText( self, wx.ID_ANY, u"R6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141221.Wrap( -1 )

		fgSizer91.Add( self.m_staticText141221, 0, wx.ALL, 5 )

		self.m_checkBox221 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_checkBox221, 0, wx.ALL, 5 )

		self.m_checkBox212 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_checkBox212, 0, wx.ALL, 5 )

		self.m_staticText141231 = wx.StaticText( self, wx.ID_ANY, u"R7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141231.Wrap( -1 )

		fgSizer91.Add( self.m_staticText141231, 0, wx.ALL, 5 )

		self.m_checkBox213 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_checkBox213, 0, wx.ALL, 5 )

		self.m_checkBox12 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_checkBox12, 0, wx.ALL, 5 )

		self.m_staticText1412411 = wx.StaticText( self, wx.ID_ANY, u"R8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1412411.Wrap( -1 )

		fgSizer91.Add( self.m_staticText1412411, 0, wx.ALL, 5 )

		self.m_checkBox21121 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_checkBox21121, 0, wx.ALL, 5 )

		self.m_checkBox111 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_checkBox111, 0, wx.ALL, 5 )

		self.m_staticText141242 = wx.StaticText( self, wx.ID_ANY, u"R9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141242.Wrap( -1 )

		fgSizer91.Add( self.m_staticText141242, 0, wx.ALL, 5 )

		self.m_checkBox461 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_checkBox461, 0, wx.ALL, 5 )

		self.m_checkBox477 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_checkBox477, 0, wx.ALL, 5 )

		self.m_staticText491 = wx.StaticText( self, wx.ID_ANY, u"R10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText491.Wrap( -1 )

		fgSizer91.Add( self.m_staticText491, 0, wx.ALL, 5 )

		self.m_checkBox4711 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_checkBox4711, 0, wx.ALL, 5 )

		self.m_checkBox4721 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_checkBox4721, 0, wx.ALL, 5 )

		self.m_staticText141251 = wx.StaticText( self, wx.ID_ANY, u"R11", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141251.Wrap( -1 )

		fgSizer91.Add( self.m_staticText141251, 0, wx.ALL, 5 )

		self.m_checkBox4731 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_checkBox4731, 0, wx.ALL, 5 )

		self.m_checkBox4761 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_checkBox4761, 0, wx.ALL, 5 )

		self.m_staticText141261 = wx.StaticText( self, wx.ID_ANY, u"R12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141261.Wrap( -1 )

		fgSizer91.Add( self.m_staticText141261, 0, wx.ALL, 5 )

		self.m_checkBox4751 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_checkBox4751, 0, wx.ALL, 5 )

		self.m_checkBox4745 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_checkBox4745, 0, wx.ALL, 5 )

		self.m_staticText141271 = wx.StaticText( self, wx.ID_ANY, u"R13", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141271.Wrap( -1 )

		fgSizer91.Add( self.m_staticText141271, 0, wx.ALL, 5 )

		self.m_checkBox47411 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_checkBox47411, 0, wx.ALL, 5 )

		self.m_checkBox47421 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_checkBox47421, 0, wx.ALL, 5 )

		self.m_staticText501 = wx.StaticText( self, wx.ID_ANY, u"R14", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText501.Wrap( -1 )

		fgSizer91.Add( self.m_staticText501, 0, wx.ALL, 5 )

		self.m_checkBox47431 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_checkBox47431, 0, wx.ALL, 5 )

		self.m_checkBox47441 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer91.Add( self.m_checkBox47441, 0, wx.ALL, 5 )


		bSizer91.Add( fgSizer91, 1, wx.EXPAND, 5 )


		bSizer8.Add( bSizer91, 1, wx.EXPAND, 5 )

		bSizer92 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText252 = wx.StaticText( self, wx.ID_ANY, u"REALITY", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText252.Wrap( -1 )

		bSizer92.Add( self.m_staticText252, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		fgSizer92 = wx.FlexGridSizer( 15, 3, 0, 0 )
		fgSizer92.SetFlexibleDirection( wx.BOTH )
		fgSizer92.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer92.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText282 = wx.StaticText( self, wx.ID_ANY, u"L", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText282.Wrap( -1 )

		fgSizer92.Add( self.m_staticText282, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText292 = wx.StaticText( self, wx.ID_ANY, u"D", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText292.Wrap( -1 )

		fgSizer92.Add( self.m_staticText292, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText143 = wx.StaticText( self, wx.ID_ANY, u"R1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText143.SetLabelMarkup( u"R1" )
		self.m_staticText143.Wrap( -1 )

		fgSizer92.Add( self.m_staticText143, 0, wx.ALL, 5 )

		self.m_checkBox211122 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox211122, 0, wx.ALL, 5 )

		self.m_checkBox2113 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox2113, 0, wx.ALL, 5 )

		self.m_staticText14112 = wx.StaticText( self, wx.ID_ANY, u"R2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14112.SetLabelMarkup( u"R2" )
		self.m_staticText14112.Wrap( -1 )

		fgSizer92.Add( self.m_staticText14112, 0, wx.ALL, 5 )

		self.m_checkBox2102 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox2102, 0, wx.ALL, 5 )

		self.m_checkBox292 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox292, 0, wx.ALL, 5 )

		self.m_staticText1414 = wx.StaticText( self, wx.ID_ANY, u"R3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1414.Wrap( -1 )

		fgSizer92.Add( self.m_staticText1414, 0, wx.ALL, 5 )

		self.m_checkBox282 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox282, 0, wx.ALL, 5 )

		self.m_checkBox272 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox272, 0, wx.ALL, 5 )

		self.m_staticText14129 = wx.StaticText( self, wx.ID_ANY, u"R4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14129.Wrap( -1 )

		fgSizer92.Add( self.m_staticText14129, 0, wx.ALL, 5 )

		self.m_checkBox262 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox262, 0, wx.ALL, 5 )

		self.m_checkBox252 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox252, 0, wx.ALL, 5 )

		self.m_staticText141212 = wx.StaticText( self, wx.ID_ANY, u"R5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141212.Wrap( -1 )

		fgSizer92.Add( self.m_staticText141212, 0, wx.ALL, 5 )

		self.m_checkBox242 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox242, 0, wx.ALL, 5 )

		self.m_checkBox232 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox232, 0, wx.ALL, 5 )

		self.m_staticText141222 = wx.StaticText( self, wx.ID_ANY, u"R6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141222.Wrap( -1 )

		fgSizer92.Add( self.m_staticText141222, 0, wx.ALL, 5 )

		self.m_checkBox222 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox222, 0, wx.ALL, 5 )

		self.m_checkBox214 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox214, 0, wx.ALL, 5 )

		self.m_staticText141232 = wx.StaticText( self, wx.ID_ANY, u"R7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141232.Wrap( -1 )

		fgSizer92.Add( self.m_staticText141232, 0, wx.ALL, 5 )

		self.m_checkBox215 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox215, 0, wx.ALL, 5 )

		self.m_checkBox13 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox13, 0, wx.ALL, 5 )

		self.m_staticText1412412 = wx.StaticText( self, wx.ID_ANY, u"R8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1412412.Wrap( -1 )

		fgSizer92.Add( self.m_staticText1412412, 0, wx.ALL, 5 )

		self.m_checkBox21122 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox21122, 0, wx.ALL, 5 )

		self.m_checkBox112 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox112, 0, wx.ALL, 5 )

		self.m_staticText141243 = wx.StaticText( self, wx.ID_ANY, u"R9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141243.Wrap( -1 )

		fgSizer92.Add( self.m_staticText141243, 0, wx.ALL, 5 )

		self.m_checkBox462 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox462, 0, wx.ALL, 5 )

		self.m_checkBox478 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox478, 0, wx.ALL, 5 )

		self.m_staticText492 = wx.StaticText( self, wx.ID_ANY, u"R10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText492.Wrap( -1 )

		fgSizer92.Add( self.m_staticText492, 0, wx.ALL, 5 )

		self.m_checkBox4712 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox4712, 0, wx.ALL, 5 )

		self.m_checkBox4722 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox4722, 0, wx.ALL, 5 )

		self.m_staticText141252 = wx.StaticText( self, wx.ID_ANY, u"R11", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141252.Wrap( -1 )

		fgSizer92.Add( self.m_staticText141252, 0, wx.ALL, 5 )

		self.m_checkBox4732 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox4732, 0, wx.ALL, 5 )

		self.m_checkBox4762 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox4762, 0, wx.ALL, 5 )

		self.m_staticText141262 = wx.StaticText( self, wx.ID_ANY, u"R12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141262.Wrap( -1 )

		fgSizer92.Add( self.m_staticText141262, 0, wx.ALL, 5 )

		self.m_checkBox4752 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox4752, 0, wx.ALL, 5 )

		self.m_checkBox4746 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox4746, 0, wx.ALL, 5 )

		self.m_staticText141272 = wx.StaticText( self, wx.ID_ANY, u"R13", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141272.Wrap( -1 )

		fgSizer92.Add( self.m_staticText141272, 0, wx.ALL, 5 )

		self.m_checkBox47412 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox47412, 0, wx.ALL, 5 )

		self.m_checkBox47422 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox47422, 0, wx.ALL, 5 )

		self.m_staticText502 = wx.StaticText( self, wx.ID_ANY, u"R14", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText502.Wrap( -1 )

		fgSizer92.Add( self.m_staticText502, 0, wx.ALL, 5 )

		self.m_checkBox47432 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox47432, 0, wx.ALL, 5 )

		self.m_checkBox47442 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer92.Add( self.m_checkBox47442, 0, wx.ALL, 5 )


		bSizer92.Add( fgSizer92, 1, wx.EXPAND, 5 )


		bSizer8.Add( bSizer92, 1, wx.EXPAND, 5 )

		bSizer93 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText253 = wx.StaticText( self, wx.ID_ANY, u"REALITY", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText253.Wrap( -1 )

		bSizer93.Add( self.m_staticText253, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		fgSizer93 = wx.FlexGridSizer( 15, 3, 0, 0 )
		fgSizer93.SetFlexibleDirection( wx.BOTH )
		fgSizer93.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer93.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText283 = wx.StaticText( self, wx.ID_ANY, u"L", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText283.Wrap( -1 )

		fgSizer93.Add( self.m_staticText283, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText293 = wx.StaticText( self, wx.ID_ANY, u"D", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText293.Wrap( -1 )

		fgSizer93.Add( self.m_staticText293, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText144 = wx.StaticText( self, wx.ID_ANY, u"R1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText144.SetLabelMarkup( u"R1" )
		self.m_staticText144.Wrap( -1 )

		fgSizer93.Add( self.m_staticText144, 0, wx.ALL, 5 )

		self.m_checkBox211123 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox211123, 0, wx.ALL, 5 )

		self.m_checkBox2114 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox2114, 0, wx.ALL, 5 )

		self.m_staticText14113 = wx.StaticText( self, wx.ID_ANY, u"R2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14113.SetLabelMarkup( u"R2" )
		self.m_staticText14113.Wrap( -1 )

		fgSizer93.Add( self.m_staticText14113, 0, wx.ALL, 5 )

		self.m_checkBox2103 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox2103, 0, wx.ALL, 5 )

		self.m_checkBox293 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox293, 0, wx.ALL, 5 )

		self.m_staticText1415 = wx.StaticText( self, wx.ID_ANY, u"R3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1415.Wrap( -1 )

		fgSizer93.Add( self.m_staticText1415, 0, wx.ALL, 5 )

		self.m_checkBox283 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox283, 0, wx.ALL, 5 )

		self.m_checkBox273 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox273, 0, wx.ALL, 5 )

		self.m_staticText141210 = wx.StaticText( self, wx.ID_ANY, u"R4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141210.Wrap( -1 )

		fgSizer93.Add( self.m_staticText141210, 0, wx.ALL, 5 )

		self.m_checkBox263 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox263, 0, wx.ALL, 5 )

		self.m_checkBox253 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox253, 0, wx.ALL, 5 )

		self.m_staticText141213 = wx.StaticText( self, wx.ID_ANY, u"R5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141213.Wrap( -1 )

		fgSizer93.Add( self.m_staticText141213, 0, wx.ALL, 5 )

		self.m_checkBox243 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox243, 0, wx.ALL, 5 )

		self.m_checkBox233 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox233, 0, wx.ALL, 5 )

		self.m_staticText141223 = wx.StaticText( self, wx.ID_ANY, u"R6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141223.Wrap( -1 )

		fgSizer93.Add( self.m_staticText141223, 0, wx.ALL, 5 )

		self.m_checkBox223 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox223, 0, wx.ALL, 5 )

		self.m_checkBox216 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox216, 0, wx.ALL, 5 )

		self.m_staticText141233 = wx.StaticText( self, wx.ID_ANY, u"R7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141233.Wrap( -1 )

		fgSizer93.Add( self.m_staticText141233, 0, wx.ALL, 5 )

		self.m_checkBox217 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox217, 0, wx.ALL, 5 )

		self.m_checkBox14 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox14, 0, wx.ALL, 5 )

		self.m_staticText1412413 = wx.StaticText( self, wx.ID_ANY, u"R8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1412413.Wrap( -1 )

		fgSizer93.Add( self.m_staticText1412413, 0, wx.ALL, 5 )

		self.m_checkBox21123 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox21123, 0, wx.ALL, 5 )

		self.m_checkBox113 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox113, 0, wx.ALL, 5 )

		self.m_staticText141244 = wx.StaticText( self, wx.ID_ANY, u"R9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141244.Wrap( -1 )

		fgSizer93.Add( self.m_staticText141244, 0, wx.ALL, 5 )

		self.m_checkBox463 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox463, 0, wx.ALL, 5 )

		self.m_checkBox479 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox479, 0, wx.ALL, 5 )

		self.m_staticText493 = wx.StaticText( self, wx.ID_ANY, u"R10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText493.Wrap( -1 )

		fgSizer93.Add( self.m_staticText493, 0, wx.ALL, 5 )

		self.m_checkBox4713 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox4713, 0, wx.ALL, 5 )

		self.m_checkBox4723 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox4723, 0, wx.ALL, 5 )

		self.m_staticText141253 = wx.StaticText( self, wx.ID_ANY, u"R11", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141253.Wrap( -1 )

		fgSizer93.Add( self.m_staticText141253, 0, wx.ALL, 5 )

		self.m_checkBox4733 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox4733, 0, wx.ALL, 5 )

		self.m_checkBox4763 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox4763, 0, wx.ALL, 5 )

		self.m_staticText141263 = wx.StaticText( self, wx.ID_ANY, u"R12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141263.Wrap( -1 )

		fgSizer93.Add( self.m_staticText141263, 0, wx.ALL, 5 )

		self.m_checkBox4753 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox4753, 0, wx.ALL, 5 )

		self.m_checkBox4747 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox4747, 0, wx.ALL, 5 )

		self.m_staticText141273 = wx.StaticText( self, wx.ID_ANY, u"R13", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141273.Wrap( -1 )

		fgSizer93.Add( self.m_staticText141273, 0, wx.ALL, 5 )

		self.m_checkBox47413 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox47413, 0, wx.ALL, 5 )

		self.m_checkBox47423 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox47423, 0, wx.ALL, 5 )

		self.m_staticText503 = wx.StaticText( self, wx.ID_ANY, u"R14", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText503.Wrap( -1 )

		fgSizer93.Add( self.m_staticText503, 0, wx.ALL, 5 )

		self.m_checkBox47433 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox47433, 0, wx.ALL, 5 )

		self.m_checkBox47443 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer93.Add( self.m_checkBox47443, 0, wx.ALL, 5 )


		bSizer93.Add( fgSizer93, 1, wx.EXPAND, 5 )


		bSizer8.Add( bSizer93, 1, wx.EXPAND, 5 )

		bSizer94 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText254 = wx.StaticText( self, wx.ID_ANY, u"REALITY", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText254.Wrap( -1 )

		bSizer94.Add( self.m_staticText254, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		fgSizer94 = wx.FlexGridSizer( 15, 3, 0, 0 )
		fgSizer94.SetFlexibleDirection( wx.BOTH )
		fgSizer94.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer94.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText284 = wx.StaticText( self, wx.ID_ANY, u"L", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText284.Wrap( -1 )

		fgSizer94.Add( self.m_staticText284, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText294 = wx.StaticText( self, wx.ID_ANY, u"D", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText294.Wrap( -1 )

		fgSizer94.Add( self.m_staticText294, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText145 = wx.StaticText( self, wx.ID_ANY, u"R1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText145.SetLabelMarkup( u"R1" )
		self.m_staticText145.Wrap( -1 )

		fgSizer94.Add( self.m_staticText145, 0, wx.ALL, 5 )

		self.m_checkBox211124 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox211124, 0, wx.ALL, 5 )

		self.m_checkBox2115 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox2115, 0, wx.ALL, 5 )

		self.m_staticText14114 = wx.StaticText( self, wx.ID_ANY, u"R2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14114.SetLabelMarkup( u"R2" )
		self.m_staticText14114.Wrap( -1 )

		fgSizer94.Add( self.m_staticText14114, 0, wx.ALL, 5 )

		self.m_checkBox2104 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox2104, 0, wx.ALL, 5 )

		self.m_checkBox294 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox294, 0, wx.ALL, 5 )

		self.m_staticText1416 = wx.StaticText( self, wx.ID_ANY, u"R3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1416.Wrap( -1 )

		fgSizer94.Add( self.m_staticText1416, 0, wx.ALL, 5 )

		self.m_checkBox284 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox284, 0, wx.ALL, 5 )

		self.m_checkBox274 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox274, 0, wx.ALL, 5 )

		self.m_staticText141214 = wx.StaticText( self, wx.ID_ANY, u"R4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141214.Wrap( -1 )

		fgSizer94.Add( self.m_staticText141214, 0, wx.ALL, 5 )

		self.m_checkBox264 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox264, 0, wx.ALL, 5 )

		self.m_checkBox254 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox254, 0, wx.ALL, 5 )

		self.m_staticText141215 = wx.StaticText( self, wx.ID_ANY, u"R5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141215.Wrap( -1 )

		fgSizer94.Add( self.m_staticText141215, 0, wx.ALL, 5 )

		self.m_checkBox244 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox244, 0, wx.ALL, 5 )

		self.m_checkBox234 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox234, 0, wx.ALL, 5 )

		self.m_staticText141224 = wx.StaticText( self, wx.ID_ANY, u"R6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141224.Wrap( -1 )

		fgSizer94.Add( self.m_staticText141224, 0, wx.ALL, 5 )

		self.m_checkBox224 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox224, 0, wx.ALL, 5 )

		self.m_checkBox218 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox218, 0, wx.ALL, 5 )

		self.m_staticText141234 = wx.StaticText( self, wx.ID_ANY, u"R7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141234.Wrap( -1 )

		fgSizer94.Add( self.m_staticText141234, 0, wx.ALL, 5 )

		self.m_checkBox219 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox219, 0, wx.ALL, 5 )

		self.m_checkBox15 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox15, 0, wx.ALL, 5 )

		self.m_staticText1412414 = wx.StaticText( self, wx.ID_ANY, u"R8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1412414.Wrap( -1 )

		fgSizer94.Add( self.m_staticText1412414, 0, wx.ALL, 5 )

		self.m_checkBox21124 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox21124, 0, wx.ALL, 5 )

		self.m_checkBox114 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox114, 0, wx.ALL, 5 )

		self.m_staticText141245 = wx.StaticText( self, wx.ID_ANY, u"R9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141245.Wrap( -1 )

		fgSizer94.Add( self.m_staticText141245, 0, wx.ALL, 5 )

		self.m_checkBox464 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox464, 0, wx.ALL, 5 )

		self.m_checkBox4710 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox4710, 0, wx.ALL, 5 )

		self.m_staticText494 = wx.StaticText( self, wx.ID_ANY, u"R10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText494.Wrap( -1 )

		fgSizer94.Add( self.m_staticText494, 0, wx.ALL, 5 )

		self.m_checkBox4714 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox4714, 0, wx.ALL, 5 )

		self.m_checkBox4724 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox4724, 0, wx.ALL, 5 )

		self.m_staticText141254 = wx.StaticText( self, wx.ID_ANY, u"R11", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141254.Wrap( -1 )

		fgSizer94.Add( self.m_staticText141254, 0, wx.ALL, 5 )

		self.m_checkBox4734 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox4734, 0, wx.ALL, 5 )

		self.m_checkBox4764 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox4764, 0, wx.ALL, 5 )

		self.m_staticText141264 = wx.StaticText( self, wx.ID_ANY, u"R12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141264.Wrap( -1 )

		fgSizer94.Add( self.m_staticText141264, 0, wx.ALL, 5 )

		self.m_checkBox4754 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox4754, 0, wx.ALL, 5 )

		self.m_checkBox4748 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox4748, 0, wx.ALL, 5 )

		self.m_staticText141274 = wx.StaticText( self, wx.ID_ANY, u"R13", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141274.Wrap( -1 )

		fgSizer94.Add( self.m_staticText141274, 0, wx.ALL, 5 )

		self.m_checkBox47414 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox47414, 0, wx.ALL, 5 )

		self.m_checkBox47424 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox47424, 0, wx.ALL, 5 )

		self.m_staticText504 = wx.StaticText( self, wx.ID_ANY, u"R14", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText504.Wrap( -1 )

		fgSizer94.Add( self.m_staticText504, 0, wx.ALL, 5 )

		self.m_checkBox47434 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox47434, 0, wx.ALL, 5 )

		self.m_checkBox47444 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer94.Add( self.m_checkBox47444, 0, wx.ALL, 5 )


		bSizer94.Add( fgSizer94, 1, wx.EXPAND, 5 )


		bSizer8.Add( bSizer94, 1, wx.EXPAND, 5 )

		bSizer95 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText255 = wx.StaticText( self, wx.ID_ANY, u"REALITY", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText255.Wrap( -1 )

		bSizer95.Add( self.m_staticText255, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		fgSizer95 = wx.FlexGridSizer( 15, 3, 0, 0 )
		fgSizer95.SetFlexibleDirection( wx.BOTH )
		fgSizer95.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer95.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText285 = wx.StaticText( self, wx.ID_ANY, u"L", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText285.Wrap( -1 )

		fgSizer95.Add( self.m_staticText285, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText295 = wx.StaticText( self, wx.ID_ANY, u"D", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText295.Wrap( -1 )

		fgSizer95.Add( self.m_staticText295, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText146 = wx.StaticText( self, wx.ID_ANY, u"R1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText146.SetLabelMarkup( u"R1" )
		self.m_staticText146.Wrap( -1 )

		fgSizer95.Add( self.m_staticText146, 0, wx.ALL, 5 )

		self.m_checkBox211125 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox211125, 0, wx.ALL, 5 )

		self.m_checkBox2116 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox2116, 0, wx.ALL, 5 )

		self.m_staticText14115 = wx.StaticText( self, wx.ID_ANY, u"R2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14115.SetLabelMarkup( u"R2" )
		self.m_staticText14115.Wrap( -1 )

		fgSizer95.Add( self.m_staticText14115, 0, wx.ALL, 5 )

		self.m_checkBox2105 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox2105, 0, wx.ALL, 5 )

		self.m_checkBox295 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox295, 0, wx.ALL, 5 )

		self.m_staticText1417 = wx.StaticText( self, wx.ID_ANY, u"R3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1417.Wrap( -1 )

		fgSizer95.Add( self.m_staticText1417, 0, wx.ALL, 5 )

		self.m_checkBox285 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox285, 0, wx.ALL, 5 )

		self.m_checkBox275 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox275, 0, wx.ALL, 5 )

		self.m_staticText141216 = wx.StaticText( self, wx.ID_ANY, u"R4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141216.Wrap( -1 )

		fgSizer95.Add( self.m_staticText141216, 0, wx.ALL, 5 )

		self.m_checkBox265 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox265, 0, wx.ALL, 5 )

		self.m_checkBox255 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox255, 0, wx.ALL, 5 )

		self.m_staticText141217 = wx.StaticText( self, wx.ID_ANY, u"R5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141217.Wrap( -1 )

		fgSizer95.Add( self.m_staticText141217, 0, wx.ALL, 5 )

		self.m_checkBox245 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox245, 0, wx.ALL, 5 )

		self.m_checkBox235 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox235, 0, wx.ALL, 5 )

		self.m_staticText141225 = wx.StaticText( self, wx.ID_ANY, u"R6", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141225.Wrap( -1 )

		fgSizer95.Add( self.m_staticText141225, 0, wx.ALL, 5 )

		self.m_checkBox225 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox225, 0, wx.ALL, 5 )

		self.m_checkBox2110 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox2110, 0, wx.ALL, 5 )

		self.m_staticText141235 = wx.StaticText( self, wx.ID_ANY, u"R7", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141235.Wrap( -1 )

		fgSizer95.Add( self.m_staticText141235, 0, wx.ALL, 5 )

		self.m_checkBox220 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox220, 0, wx.ALL, 5 )

		self.m_checkBox16 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox16, 0, wx.ALL, 5 )

		self.m_staticText1412415 = wx.StaticText( self, wx.ID_ANY, u"R8", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1412415.Wrap( -1 )

		fgSizer95.Add( self.m_staticText1412415, 0, wx.ALL, 5 )

		self.m_checkBox21125 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox21125, 0, wx.ALL, 5 )

		self.m_checkBox115 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox115, 0, wx.ALL, 5 )

		self.m_staticText141246 = wx.StaticText( self, wx.ID_ANY, u"R9", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141246.Wrap( -1 )

		fgSizer95.Add( self.m_staticText141246, 0, wx.ALL, 5 )

		self.m_checkBox465 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox465, 0, wx.ALL, 5 )

		self.m_checkBox4715 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox4715, 0, wx.ALL, 5 )

		self.m_staticText495 = wx.StaticText( self, wx.ID_ANY, u"R10", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText495.Wrap( -1 )

		fgSizer95.Add( self.m_staticText495, 0, wx.ALL, 5 )

		self.m_checkBox4716 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox4716, 0, wx.ALL, 5 )

		self.m_checkBox4725 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox4725, 0, wx.ALL, 5 )

		self.m_staticText141255 = wx.StaticText( self, wx.ID_ANY, u"R11", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141255.Wrap( -1 )

		fgSizer95.Add( self.m_staticText141255, 0, wx.ALL, 5 )

		self.m_checkBox4735 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox4735, 0, wx.ALL, 5 )

		self.m_checkBox4765 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox4765, 0, wx.ALL, 5 )

		self.m_staticText141265 = wx.StaticText( self, wx.ID_ANY, u"R12", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141265.Wrap( -1 )

		fgSizer95.Add( self.m_staticText141265, 0, wx.ALL, 5 )

		self.m_checkBox4755 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox4755, 0, wx.ALL, 5 )

		self.m_checkBox4749 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox4749, 0, wx.ALL, 5 )

		self.m_staticText141275 = wx.StaticText( self, wx.ID_ANY, u"R13", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText141275.Wrap( -1 )

		fgSizer95.Add( self.m_staticText141275, 0, wx.ALL, 5 )

		self.m_checkBox47415 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox47415, 0, wx.ALL, 5 )

		self.m_checkBox47425 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox47425, 0, wx.ALL, 5 )

		self.m_staticText505 = wx.StaticText( self, wx.ID_ANY, u"R14", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText505.Wrap( -1 )

		fgSizer95.Add( self.m_staticText505, 0, wx.ALL, 5 )

		self.m_checkBox47435 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox47435, 0, wx.ALL, 5 )

		self.m_checkBox47445 = wx.CheckBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer95.Add( self.m_checkBox47445, 0, wx.ALL, 5 )


		bSizer95.Add( fgSizer95, 1, wx.EXPAND, 5 )


		bSizer8.Add( bSizer95, 1, wx.EXPAND, 5 )


		bSizer16.Add( bSizer8, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer16 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class MyPanel5
###########################################################################

class MyPanel5 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )


	def __del__( self ):
		pass


###########################################################################
## Class OccupationFinder
###########################################################################

class OccupationFinder ( main ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		main.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		bSizer27 = wx.BoxSizer( wx.HORIZONTAL )

		fgSizer17 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer17.AddGrowableCol( 0 )
		fgSizer17.SetFlexibleDirection( wx.BOTH )
		fgSizer17.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_searchCtrl2 = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.m_searchCtrl2.ShowSearchButton( True )
		self.m_searchCtrl2.ShowCancelButton( False )
		fgSizer17.Add( self.m_searchCtrl2, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )

		self.nomor_jawaban = wx.StaticText( self, wx.ID_ANY, u"Nomor Jawaban", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nomor_jawaban.Wrap( -1 )

		fgSizer17.Add( self.nomor_jawaban, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		m_choice4Choices = [ u"1", u"2", u"3", u"4", u"5", u"6", u"7", wx.EmptyString ]
		self.m_choice4 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice4Choices, 0 )
		self.m_choice4.SetSelection( 4 )
		fgSizer17.Add( self.m_choice4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.OccupationF_tombol_ok = wx.Button( self, wx.ID_ANY, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer17.Add( self.OccupationF_tombol_ok, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer27.Add( fgSizer17, 1, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer11.Add( bSizer27, 0, wx.EXPAND, 5 )

		m_listBox3Choices = [ u"1", u"2", u"3", u"4", u"5", u"6", wx.EmptyString ]
		self.m_listBox3 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox3Choices, wx.LB_ALWAYS_SB )
		bSizer11.Add( self.m_listBox3, 1, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()

		# Connect Events
		self.OccupationF_tombol_ok.Bind( wx.EVT_BUTTON, self.OccupationF_tombol_okOnButtonClick )
		self.m_listBox3.Bind( wx.EVT_LISTBOX_DCLICK, self.btn_occupationfinder )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OccupationF_tombol_okOnButtonClick( self, event ):
		event.Skip()

	def btn_occupationfinder( self, event ):
		event.Skip()


###########################################################################
## Class MyPanel9
###########################################################################

class MyPanel9 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )


	def __del__( self ):
		pass


###########################################################################
## Class ss
###########################################################################

class ss ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.AddGrowableCol( 0 )
		fgSizer5.AddGrowableCol( 1 )
		fgSizer5.AddGrowableRow( 0 )
		fgSizer5.AddGrowableRow( 1 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_grid6 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid6.CreateGrid( 20, 20 )
		self.m_grid6.EnableEditing( True )
		self.m_grid6.EnableGridLines( True )
		self.m_grid6.EnableDragGridSize( False )
		self.m_grid6.SetMargins( 0, 0 )

		# Columns
		self.m_grid6.EnableDragColMove( False )
		self.m_grid6.EnableDragColSize( True )
		self.m_grid6.SetColLabelSize( 30 )
		self.m_grid6.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid6.EnableDragRowSize( True )
		self.m_grid6.SetRowLabelSize( 80 )
		self.m_grid6.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid6.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer5.Add( self.m_grid6, 5, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( fgSizer5 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class Page4
###########################################################################

class Page4 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		fgSizer5 = wx.FlexGridSizer( 1, 1, 0, 0 )
		fgSizer5.AddGrowableCol( 0 )
		fgSizer5.AddGrowableRow( 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_grid6 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid6.CreateGrid( 20, 20 )
		self.m_grid6.EnableEditing( True )
		self.m_grid6.EnableGridLines( True )
		self.m_grid6.EnableDragGridSize( False )
		self.m_grid6.SetMargins( 0, 0 )

		# Columns
		self.m_grid6.EnableDragColMove( False )
		self.m_grid6.EnableDragColSize( True )
		self.m_grid6.SetColLabelSize( 30 )
		self.m_grid6.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid6.EnableDragRowSize( True )
		self.m_grid6.SetRowLabelSize( 80 )
		self.m_grid6.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid6.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		fgSizer5.Add( self.m_grid6, 5, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( fgSizer5 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class WindowsPopUp
###########################################################################

class WindowsPopUp ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


