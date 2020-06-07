import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from Admin_pannel import ADMIN_PANNEL as admin

class ADMIN_LOGIN:

    def jump_admin(self):
        self.top.destroy()
        admin()

    def Cancel_login(self):
        msg = messagebox.askyesno('Login page','Are you sure, you want to cancel login?')
        if (msg):
            exit()
    
    def login_admin(self):
        name = self.Entry_userid.get()
        password = self.Entry_passwd.get()

        if (name == "iamadmin") and (password == "testqwerty123"):
            self.jump_admin()
        else:
            self.Label_warning['text'] = "invalid username or password!"

    def __init__(self):

        self.top = tk.Tk()
        '''This class configures and populates the toplevel window.
           self.top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Berlin Sans FB Demi} -size 12 -weight bold"
        font9 = "-family {ROG Fonts} -size 20"

        self.top.geometry("600x450+650+150")
        self.top.minsize(148, 1)
        self.top.maxsize(1924, 1055)
        self.top.resizable(0, 0)
        self.top.title("Login")

        self.Button_login = tk.Button(self.top)
        self.Button_login.place(relx=0.367, rely=0.667, height=43, width=89)
        self.Button_login.configure(activeforeground="#f9f9f9", disabledforeground="#a3a3a3", font=font10, foreground="#000000")
        self.Button_login.configure(highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Login''', command = self.login_admin)

        self.Button_cancel = tk.Button(self.top)
        self.Button_cancel.place(relx=0.55, rely=0.667, height=43, width=86)
        self.Button_cancel.configure(activeforeground="#fcfcfc", disabledforeground="#a3a3a3", font=font10, foreground="#000000", highlightbackground="#d9d9d9")
        self.Button_cancel.configure(highlightcolor="black", pady="0", text='''Cancel''', command=self.Cancel_login)

        self.Entry_userid = tk.Entry(self.top)
        self.Entry_userid.place(relx=0.333, rely=0.378, height=34, relwidth=0.44)
        self.Entry_userid.configure(disabledforeground="#a3a3a3", font="TkFixedFont", foreground="#000000", insertbackground="black")

        
        self.Label_userid = tk.Label(self.top)
        self.Label_userid.place(relx=0.117, rely=0.378, height=36, width=80)
        self.Label_userid.configure(disabledforeground="#a3a3a3", font=font10, foreground="#000000", text='''User Id''')

        self.Label_password = tk.Label(self.top)
        self.Label_password.place(relx=0.117, rely=0.489, height=36, width=88)
        self.Label_password.configure(disabledforeground="#a3a3a3", font=font10, foreground="#000000", text='''Password''')

        self.Entry_passwd = tk.Entry(self.top)
        self.Entry_passwd.place(relx=0.333, rely=0.489, height=34, relwidth=0.44)
        self.Entry_passwd.configure(disabledforeground="#a3a3a3", font="TkFixedFont", foreground="#000000", insertbackground="black")

        self.Labelframe_login = tk.LabelFrame(self.top)
        self.Labelframe_login.place(relx=0.367, rely=0.044, relheight=0.167, relwidth=0.25)
        self.Labelframe_login.configure(relief='groove',foreground="black")

        self.Label_lg = tk.Label(self.Labelframe_login)
        self.Label_lg.place(relx=0.067, rely=0.133, height=56, width=127, bordermode='ignore')
        self.Label_lg.configure(disabledforeground="#a3a3a3", font=font9, foreground="#000000", text='''LOGIN''')
        

        text = tk.StringVar()
        text = ''
        self.Label_warning = tk.Label(self.top, text = text)
        self.Label_warning.place(relx=0.233, rely=0.244, height=36, width=252)
        self.Label_warning.configure(disabledforeground="#a3a3a3", foreground="#000000", font=font10)

        self.top.mainloop()