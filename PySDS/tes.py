#!usr/bin/python
import wx


class Frame(wx.Frame):
    
    def __init__(self,*args,**kwds):
        super(Frame,self).__init__(*args,**kwds)
        self.start_image = wx.Image("binakarir2.png") 
        self.start_image.Rescale(200, 100) 
        self.image = wx.BitmapFromImage(self.start_image) 
        self.mypic = wx.StaticBitmap(self, -1, self.image, wx.DefaultPosition, style=wx.BITMAP_TYPE_PNG)  




if __name__=="__main__":
    root =wx.App()
    frame = Frame(None).Show()
    root.MainLoop()
    