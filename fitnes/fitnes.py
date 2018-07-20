import tkinter as tk

class Window(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)
        self.master = master
        self.master.geometry("400x200")
        self.master.title("Fitnes Center")

        self.frame1 = tk.Frame(self.master,width =200 ,height =200)
        self.frame1.grid(row=0,column=0)
        self.label1 =tk.Label(self.frame1,text="LOGIN FITNES CENTER")
        self.label1.grid(row=0,column=0)
        
        self.frame2 = tk.Frame(self.master)
        self.frame2.grid(row=1,column=0)
        
        self.label = tk.Label(self.frame2,text="Username",padx =50)
        self.label.grid(row=0,column=0)
        self.label = tk.Label(self.frame2,text="Password")
        self.label.grid(row=1,column=0)
        self.textbox =tk.Entry(self.frame2)
        self.textbox.grid(row=0,column=1)
        self.textbox =tk.Entry(self.frame2)
        self.textbox.grid(row=1,column=1)
        
        self.button1=tk.Button(self.frame2,text="clear")
        self.button1.grid(row=2,column=0)
        self.button2=tk.Button(self.frame2,text="login")
        self.button2.grid(row=2,column=1)
        
        self.frame3=tk.Frame(self.master)
        self.frame3.grid(row=2,column=0)
        
        self.label1=tk.Label(self.frame3,text="Don't have an account yet?")
        self.label1.grid(row=0,column=0)
        
        self.button3=tk.Button(self.frame3,text="Register")
        self.button3.grid(row=1,column=0)
        self.button3.bind("<Button-1>",self.register)
        
        
    def register(self,event):
        #self.master.withdraw()
        self.top =tk.Toplevel()
        self.DJB_Fitness_Tracker(self.top)
        print ("okay")


    def DJB_Fitness_Tracker(self,parent):
        self.top = parent
        self.top.geometry("400x250")
        self.top.title("Register")
        
        self.Frame = tk.Frame(self.top)
        self.Frame.grid(row=0,column=0)
        
        self.Label=tk.Label(self.Frame,text="Register",anchor="center")
        self.Label.grid(row=0,column=0)
        
        self.Frame2=tk.Frame(self.top)
        self.Frame2.grid(row=1,column=0)
        
        self.username = tk.Label(self.Frame2,text="Username")
        self.username.grid(row=0,column=0)
        self.password=tk.Label(self.Frame2,text="Password")
        self.password.grid(row=1,column=0)
        self.confirmpassword = tk.Label(self.Frame2,text="Confirm Password")
        self.confirmpassword.grid(row=2,column=0)
        self.aim = tk.Label(self.Frame2,text="Your Aim")
        self.aim.grid(row=3,column=0)
    
    
        self.username = tk.Entry(self.Frame2,text="Username")
        self.username.grid(row=0,column=1)
        self.password=tk.Entry(self.Frame2,text="Password")
        self.password.grid(row=1,column=1)
        self.confirmpassword = tk.Entry(self.Frame2,text="Confirm Password")
        self.confirmpassword.grid(row=2,column=1)
        
        self.radiobutton1 =tk.Radiobutton(self.Frame2, text ="Gain Muscle")
        self.radiobutton1.grid(row=3,column=1)
        self.radiobutton2 =tk.Radiobutton(self.Frame2, text="Maintain Fitnes")
        self.radiobutton2.grid(row=4,column=1)
        self.radiobutton3 =tk.Radiobutton(self.Frame2,text ="Get Fit")
        self.radiobutton3.grid(row=5,column=1)
    
        self.button1 = tk.Button(self.Frame2,text="Clear")
        self.button1.grid(row=6,column=0)
        self.button2 = tk.Button(self.Frame2,text="Login")
        self.button2.grid(row=6,column=1)
    
        
def main(): 
    root = tk.Tk()
    app = Window(root)
    root.mainloop()

if __name__ == '__main__':
    main()
