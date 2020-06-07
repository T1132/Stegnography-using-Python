import sys
import tkinter as tk
import tkinter.ttk as ttk
from data_insert import DATA_INSERT as insert
from data_VIEW import DATA_VIEW as view

class ADMIN_PANNEL:

    def exit(self):
        exit()

    def open_data_insert(self):
        insert()
        
    def open_data_view(self):
        view()

    def __init__(self):

        self.top = tk.Tk()
        '''This class configures and populates the self.toplevel window.
           self.top is the self.toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        self.top.geometry("739x616+650+150")
        self.top.minsize(152, 1)
        self.top.maxsize(1924, 1055)
        self.top.resizable(0, 0)
        self.top.title("ADMIN PANNEL")
        self.top.configure(background="#d9d9d9")
        self.top.configure(highlightbackground="#d9d9d9")
        self.top.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(self.top)
        self.Canvas1.place(relx=0.041, rely=0.049, relheight=0.898
                , relwidth=0.939)
        self.Canvas1.configure(background="#d9d9d9", borderwidth="2", highlightbackground="#000000", highlightcolor="black", relief="ridge")
        self.Canvas1.configure(insertbackground="#0080c0", selectbackground="#c4c4c4", selectforeground="#000000")

        self.Label1 = tk.Label(self.Canvas1)
        self.Label1.place(relx=0.259, rely=0.036, height=47, width=324)
        self.Label1.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9", disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", text='''DATABASE ADMIN CONSOLE''')

        self.Label2 = tk.Label(self.Canvas1)
        self.Label2.place(relx=0.014, rely=0.145, height=77, width=674)
        self.Label2.configure(activeforeground="#000000", background="#a5a5a5", disabledforeground="#a3a3a3", foreground="#000000")
        self.Label2.configure(highlightbackground="#000000", highlightcolor="#000000", text='''DATABASE COMMAND''')

        self.Label3 = tk.Label(self.Canvas1)
        self.Label3.place(relx=0.014, rely=0.362, height=47, width=403)
        self.Label3.configure(background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000", text='''INSERT''')

        self.Label4 = tk.Label(self.Canvas1)
        self.Label4.place(relx=0.014, rely=0.47, height=37, width=393)
        self.Label4.configure(background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000", text='''VIEW''')

        self.Label5 = tk.Label(self.Canvas1)
        self.Label5.place(relx=0.029, rely=0.579, height=37, width=375)
        self.Label5.configure(background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000", text='''EXIT''')

        self.Button1 = tk.Button(self.Canvas1)
        self.Button1.place(relx=0.607, rely=0.362, height=35, width=90)
        self.Button1.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Enter''', command = self.open_data_insert)


        self.Button2 = tk.Button(self.Canvas1)
        self.Button2.place(relx=0.607, rely=0.47, height=35, width=90)
        self.Button2.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9",disabledforeground="#a3a3a3", foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Show''', command = self.open_data_view)

        self.Button3 = tk.Button(self.Canvas1)
        self.Button3.place(relx=0.605, rely=0.579, height=35, width=90)
        self.Button3.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Exit''', command = self.exit)

        self.menubar = tk.Menu(self.top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        self.top.configure(menu = self.menubar)

        self.top.mainloop()

    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = tk.Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9", activeborderwidth="1", activeforeground="black", background="#d9d9d9", borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10", foreground="black")
        Popupmenu1.post(event.x_root, event.y_root)

