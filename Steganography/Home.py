import sys
from tkinter import messagebox
from encoder import ENCODER as encode
from decoder import DECODER as decode
import tkinter as tk
import tkinter.ttk as ttk

class HOME:

    def tell_about_me(self):
        messagebox.showinfo("About Us",'himeshnishnishant1@gmail.com')

    def run_encoder(self):
        self.top.destroy()
        encode()
    
    def run_decoder(self):
        self.top.destroy()
        decode()

    def __init__(self):
        self.top = tk.Tk()
        '''This class configures and populates the toplevel window.
           self.top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 12"
        font9 = "-family {Segoe UI Black} -size 12 -weight bold"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        self.top.geometry("600x450+591+218")
        self.top.minsize(148, 1)
        self.top.maxsize(1924, 1055)
        self.top.resizable(0, 0)
        self.top.title("Home")
        self.top.configure(background="#d9d9d9")

        self.TFrame1 = ttk.Frame(self.top)
        self.TFrame1.place(relx=0.017, rely=0.022, relheight=0.967
                , relwidth=0.975)
        self.TFrame1.configure(relief='groove', borderwidth="2")

        self.TLabel1 = ttk.Label(self.TFrame1)
        self.TLabel1.place(relx=0.137, rely=0.046, height=44, width=415)
        self.TLabel1.configure(background="#d9d9d9", foreground="#000000", font=font9, relief="flat", anchor='w', justify='center')
        self.TLabel1.configure(text='''Welcome to our steganography software''')

        self.TLabel2 = ttk.Label(self.TFrame1)
        self.TLabel2.place(relx=0.239, rely=0.184, height=54, width=265)
        self.TLabel2.configure(background="#d9d9d9", foreground="#000000", font=font10, relief="flat", anchor='w')
        self.TLabel2.configure(justify='center', text='''Choose what you want to do:''')

        self.TButton_encoder = ttk.Button(self.TFrame1)
        self.TButton_encoder.place(relx=0.103, rely=0.368, height=80, width=178)
        self.TButton_encoder.configure(takefocus="", text='''ENCODER''', command = self.run_encoder)

        self.TButton_decoder = ttk.Button(self.TFrame1)
        self.TButton_decoder.place(relx=0.564, rely=0.368, height=80, width=178)
        self.TButton_decoder.configure(takefocus="", text='''DECODER''', command = self.run_decoder)

        self.Labelframe_about = tk.LabelFrame(self.TFrame1)
        self.Labelframe_about.place(relx=0.359, rely=0.759, relheight=0.172
                , relwidth=0.256)
        self.Labelframe_about.configure(relief='groove', foreground="black", text='''About Us''', background="#d9d9d9")

        self.TButton_about = ttk.Button(self.Labelframe_about)
        self.TButton_about.place(relx=0.133, rely=0.4, height=30, width=108
                , bordermode='ignore')
        self.TButton_about.configure(takefocus="")
        self.TButton_about.configure(text='''Contact Us''')
        self.TButton_about.configure(command = self.tell_about_me)

        self.top.mainloop()






