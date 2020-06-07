import sys
import tkinter as tk
import tkinter.ttk as ttk
from database import Database

class DATA_VIEW:

    def show_data(self):
        conn = Database()
        data = conn.view()
        name = []
        email = []
        password = []
        for record in data:
            name.append(record[0])
            email.append(record[1])
            password.append(record[2])
        
        for i in range(len(name)):
            self.Text1.insert(tk.END,str("\nname = "+str(name[i])+"\nemail = "+str(email[i])+"\npassword = "+str(password[i])+"\n"))            

    def __init__(self):
        
        self.top = tk.Tk()
        '''This class configures and populates the self.toplevel window.
           self.top is the self.toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI Emoji} -size 10"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        self.top.geometry("600x450+650+150")
        self.top.minsize(152, 1)
        self.top.maxsize(1924, 1055)
        self.top.resizable(0, 0)
        self.top.title("DATA VIEW")
        self.top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.083, rely=0.044, height=47, width=523)
        self.Label1.configure(activebackground="#c0c0c0", activeforeground="#000000", background="#c0c0c0", disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000",text='''VIEW''')

        self.TButton1 = ttk.Button(self.top)
        self.TButton1.place(relx=0.117, rely=0.2, height=51, width=479)
        self.TButton1.configure(takefocus="", text='''SHOW''', command = self.show_data)

        self.Text1 = tk.Text(self.top)
        self.Text1.place(relx=0.1, rely=0.378, relheight=0.596, relwidth=0.857)
        self.Text1.configure(background="white", font=font9, foreground="black", highlightbackground="#d9d9d9", highlightcolor="black")
        self.Text1.configure(insertbackground="black", selectbackground="#c4c4c4", selectforeground="black", wrap="word")

        self.top.mainloop()

    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = tk.Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9", activeborderwidth="1",activeforeground="black",background="#d9d9d9", borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10", foreground="black")
        Popupmenu1.post(event.x_root, event.y_root)





