import sys
import tkinter as tk
import tkinter.ttk as ttk
from database import Database

class DATA_INSERT:

    def insert_data(self):
        conn = Database()
        name = self.Entry1.get()
        email = self.Entry1_5.get()
        password = self.Entry1_4.get()
        conn.add(name, email, password)

    def __init__(self):

        self.top = tk.Tk()
        '''This class configures and populates the self.toplevel window.
           self.top is the self.toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        self.top.geometry("600x450+650+150")
        self.top.minsize(152, 1)
        self.top.maxsize(1924, 1055)
        self.top.resizable(0, 0)
        self.top.title("DATA INSERTION")
        self.top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.083, rely=0.089, height=57, width=493)
        self.Label1.configure(background="#c0c0c0", disabledforeground="#a3a3a3", foreground="#000000", text='''INSERT DATA''')

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.1, rely=0.311, height=37, width=143)
        self.Label2.configure(background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000", text='''USER NAME''')

        self.Label2_2 = tk.Label(self.top)
        self.Label2_2.place(relx=0.1, rely=0.444, height=37, width=143)
        self.Label2_2.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9", disabledforeground="#a3a3a3")
        self.Label2_2.configure(foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", text='''EMAIL''')

        self.Label2_3 = tk.Label(self.top)
        self.Label2_3.place(relx=0.1, rely=0.578, height=37, width=143)
        self.Label2_3.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9", disabledforeground="#a3a3a3")
        self.Label2_3.configure(foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", text='''PASSWORD''')

        self.Entry1 = tk.Entry(self.top)
        self.Entry1.place(relx=0.417, rely=0.311,height=34, relwidth=0.473)
        self.Entry1.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont", foreground="#000000", insertbackground="black")

        self.Entry1_4 = tk.Entry(self.top)
        self.Entry1_4.place(relx=0.417, rely=0.578,height=34, relwidth=0.473)
        self.Entry1_4.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9")
        self.Entry1_4.configure(highlightcolor="black", insertbackground="black", selectbackground="#c4c4c4", selectforeground="black")

        self.Entry1_5 = tk.Entry(self.top)
        self.Entry1_5.place(relx=0.417, rely=0.444,height=34, relwidth=0.473)
        self.Entry1_5.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9")
        self.Entry1_5.configure(highlightcolor="black", insertbackground="black", selectbackground="#c4c4c4", selectforeground="black")

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.35, rely=0.778, height=45, width=150)
        self.Button1.configure(activebackground="#ececec",activeforeground="#000000", background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''INSERT''', command = self.insert_data)\

        self.top.mainloop()

    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = tk.Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9", activeborderwidth="1", activeforeground="black", background="#d9d9d9", borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10", foreground="black")
        Popupmenu1.post(event.x_root, event.y_root)





