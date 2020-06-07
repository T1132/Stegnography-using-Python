import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from database import Database
from Home import HOME as home
from admin_login import ADMIN_LOGIN as admin_log

class LOGIN:

    def admin_login(self):
        self.top.destroy()
        admin_log()

    def jump_home(self):
        self.top.destroy()
        home()

    def Cancel_login(self):
        msg = messagebox.askyesno('Login page','Are you sure, you want to cancel login?')
        if (msg):
            exit()
    
    def login_usr(self):
        conn = Database()
        name = self.Entry_userid.get()
        password = self.Entry_passwd.get()
        query = '''select * from detail where name = "'''+name+'''" and pwd = "'''+password+'''";'''
        data = conn.run(query)
        passed = False
        for record in data:
            if record[0] == name and record[2] == password:
                passed = True
                break

        if passed:
            self.jump_home()
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
        self.Button_login.configure(activeforeground="white", disabledforeground="#a3a3a3", font=font10, foreground="#000000", highlightbackground="#d9d9d9")
        self.Button_login.configure(highlightcolor="black", pady="0", text='''Login''', command = self.login_usr)

        self.Button_cancel = tk.Button(self.top)
        self.Button_cancel.place(relx=0.55, rely=0.667, height=43, width=86)
        self.Button_cancel.configure(activeforeground="white", disabledforeground="#a3a3a3", font=font10, foreground="#000000", highlightbackground="#d9d9d9")
        self.Button_cancel.configure(highlightcolor="black", pady="0", text='''Cancel''', command=self.Cancel_login)

        self.Button_admin = tk.Button(self.top)
        self.Button_admin.place(relx=0.83, rely=0.9, height=43, width=98)
        self.Button_admin.configure(activeforeground="white", disabledforeground="#a3a3a3", font=font10, foreground="#000000", highlightbackground="#d9d9d9")
        self.Button_admin.configure(highlightcolor="black", pady="0", text='''Admin Login''', command=self.admin_login)

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
        self.Labelframe_login.configure(relief='groove')
        self.Labelframe_login.configure(foreground="black")

        self.Label_lg = tk.Label(self.Labelframe_login)
        self.Label_lg.place(relx=0.067, rely=0.133, height=56, width=127, bordermode='ignore')
        self.Label_lg.configure(disabledforeground="#a3a3a3", font=font9, foreground="#000000", text='''LOGIN''')

        text = tk.StringVar()
        text = ''
        self.Label_warning = tk.Label(self.top, text = text)
        self.Label_warning.place(relx=0.233, rely=0.244, height=36, width=252)
        self.Label_warning.configure(disabledforeground="#a3a3a3", foreground="#000000", font=font10)

        self.top.mainloop()

if __name__ == "__main__":
    LOGIN()