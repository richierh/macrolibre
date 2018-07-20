#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.14
# In conjunction with Tcl version 8.6
#    Jul 18, 2018 09:58:24 AM

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import login_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    login_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    login_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font11 = "-family {Century Gothic} -size 20 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font12 = "-family {Century Gothic} -size 12 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font13 = "-family {Century Gothic} -size 11 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font14 = "-family {Century Gothic} -size 12 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font15 = "-family {Century Gothic} -size 40 -weight bold "  \
            "-slant roman -underline 1 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("599x414+804+153")
        top.title("DJB FITNESS Tracker")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=-0.02, rely=-0.02, relheight=1.03, relwidth=1.03)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#2653a0")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=615)

        self.Entry1 = Entry(self.Frame1)
        self.Entry1.place(relx=0.41, rely=0.42,height=20, relwidth=0.27)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font10)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")
        

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.26, rely=0.42, height=21, width=79)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#2653a0")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font12)
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Username''')

        self.Label3 = Label(self.Frame1)
        self.Label3.place(relx=0.26, rely=0.49, height=27, width=78)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#2653a0")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font12)
        self.Label3.configure(foreground="#ffffff")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Password''')

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.57, rely=0.59, height=33, width=57)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=login_support.triggerbutton)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font13)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Log in''')

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.49, rely=0.89, height=33, width=72)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(command=login_support.triggerbutton)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font13)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Register''')

        self.Label4 = Label(self.Frame1)
        self.Label4.place(relx=0.37, rely=0.82, height=25, width=192)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#2653a0")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font14)
        self.Label4.configure(foreground="#ffffff")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Don't have an account?''')

        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.39, rely=0.59, height=33, width=54)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font=font13)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Clear''')

        self.Label5 = Label(self.Frame1)
        self.Label5.place(relx=0.03, rely=0.05, height=290, width=124)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#2653a0")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font15)
        self.Label5.configure(foreground="#ffffff")
        self.Label5.configure(highlightbackground="#f0f0f0")
        self.Label5.configure(highlightcolor="black")
        self._img1 = PhotoImage(file="./gym.png")
        self.Label5.configure(image=self._img1)
        self.Label5.configure(text='''TRACKER''')

        self.Label7 = Label(self.Frame1)
        self.Label7.place(relx=0.26, rely=0.05, height=69, width=299)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="#000000")
        self.Label7.configure(background="#2653a0")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(font=font15)
        self.Label7.configure(foreground="#ffffff")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''DJB FITNESS''')

        self.Entry3 = Entry(self.Frame1)
        self.Entry3.place(relx=0.41, rely=0.49,height=20, relwidth=0.27)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font=font10)
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(highlightbackground="#d9d9d9")
        self.Entry3.configure(highlightcolor="black")
        self.Entry3.configure(insertbackground="black")
        self.Entry3.configure(selectbackground="#c4c4c4")
        self.Entry3.configure(selectforeground="black")
        self.Entry3.configure(takefocus="0")
        self.Entry3.configure(show='*')

        self.Label7_1 = Label(self.Frame1)
        self.Label7_1.place(relx=0.26, rely=0.21, height=69, width=299)
        self.Label7_1.configure(activebackground="#f9f9f9")
        self.Label7_1.configure(activeforeground="#000000")
        self.Label7_1.configure(background="#2653a0")
        self.Label7_1.configure(disabledforeground="#a3a3a3")
        self.Label7_1.configure(font=font15)
        self.Label7_1.configure(foreground="#ffffff")
        self.Label7_1.configure(highlightbackground="#d9d9d9")
        self.Label7_1.configure(highlightcolor="black")
        self.Label7_1.configure(text='''TRACKER''')

        self.Frame2 = Frame(self.Frame1)
        self.Frame2.place(relx=0.07, rely=0.68, relheight=0.13, relwidth=0.89)
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief=GROOVE)
        self.Frame2.configure(background="#2653a0")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")
        self.Frame2.configure(width=545)

        self.Label6_1 = Label(self.Frame1)
        self.Label6_1.place(relx=0.16, rely=0.7, height=43, width=431)
        self.Label6_1.configure(activebackground="#f9f9f9")
        self.Label6_1.configure(activeforeground="black")
        self.Label6_1.configure(background="#2653a0")
        self.Label6_1.configure(disabledforeground="#a3a3a3")
        self.Label6_1.configure(font=font11)
        self.Label6_1.configure(foreground="#ffffff")
        self.Label6_1.configure(highlightbackground="#d9d9d9")
        self.Label6_1.configure(highlightcolor="black")
        self.Label6_1.configure(text='''YOUR GUIDE TO FITNESS SUCCESS''')

        self.menubar = Menu(top,font=font9,bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)








if __name__ == '__main__':
    vp_start_gui()



