import sys
import os
from PIL import Image, ImageTk
from tkinter import filedialog
from decoder_BPCS import Decoder_BPCS
from decoder_LSB import Decoder_LSB
import tkinter as tk
import tkinter.ttk as ttk

class DECODER:

    def var_chioce(self):
        self.choice = self.var_technique.get()
        if self.choice == 1:
            self.exploit_for_LSB()
        elif self.choice == 2:
            self.exploit_for_BPCS()

    def exploit_for_BPCS(self):
    
        self.secret_message = Decoder_BPCS.decoder_module(Decoder_BPCS,self.imagefilename, self.input_image_width, self.input_image_height
        ,self.TEntry_key.get())

        self.Scrolledtext_message.insert(tk.INSERT,self.secret_message)
    
    def exploit_for_LSB(self):
    
        self.secret_message = Decoder_LSB.decoder_module(Decoder_LSB,self.imagefilename, self.input_image_width, self.input_image_height
        , self.TEntry_key.get())

        self.Scrolledtext_message.insert(tk.INSERT,self.secret_message)

    def FileDialogForInputImage(self):
        
        self.imagefilename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =(("png files","*.png"),("All files","*")))
        
        self.img_input = Image.open(self.imagefilename)
        self.input_image_width, self.input_image_height = self.img_input.size 
        newsize = (501, 400) 
        self.img_input_resize = self.img_input.resize(newsize)  
        self.Canvas_input.image = ImageTk.PhotoImage(self.img_input_resize)
        self.Canvas_input.create_image(0, 0, image = self.Canvas_input.image, anchor = 'nw')
    
    def __init__(self):

        self.top = tk.Tk()
        '''This class configures and populates the toplevel window.
           self.top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font12 = "-family {Segoe UI Semibold} -size 19 -weight bold"
        font14 = "-family {Segoe UI} -size 15"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        self.top.geometry("1501x700+0+0")
        self.top.minsize(148, 1)
        self.top.maxsize(1924, 1055)
        self.top.resizable(0, 0)
        self.top.title("decoder")
        self.top.configure(background="#d9d9d9")

        self.TFrame_main = ttk.Frame(self.top)
        self.TFrame_main.place(relx=0.007, rely=0.014, relheight=0.979
                , relwidth=0.989)
        self.TFrame_main.configure(relief='groove', borderwidth="2")

        self.TSeparator1 = ttk.Separator(self.TFrame_main)
        self.TSeparator1.place(relx=0.466, rely=0.009, relheight=0.981)
        self.TSeparator1.configure(orient="vertical")

        self.TFrame_input = ttk.Frame(self.TFrame_main)
        self.TFrame_input.place(relx=0.007, rely=0.015, relheight=0.724
                , relwidth=0.456)
        self.TFrame_input.configure(relief='groove', borderwidth="2")

        self.Canvas_input = tk.Canvas(self.TFrame_input)
        self.Canvas_input.place(relx=0.133, rely=0.161, relheight=0.806
                , relwidth=0.74)
        self.Canvas_input.configure(background="#d9d9d9", borderwidth="2", insertbackground="black", relief="ridge", selectbackground="#c4c4c4")
        self.Canvas_input.configure(selectforeground="black")

        self.TSeparator_input = ttk.Separator(self.TFrame_input)
        self.TSeparator_input.place(relx=0.025, rely=0.133, relwidth=0.948)

        self.TLabel_input = ttk.Label(self.TFrame_input)
        self.TLabel_input.place(relx=0.443, rely=0.02, height=50, width=90)
        #self.TLabel_input.configure(background="#d9d9d9")
        self.TLabel_input.configure(foreground="#000000", font=font12, relief="flat", anchor='w', justify='center', text='''Input''')

        self.TFrame_functions = ttk.Frame(self.TFrame_main)
        self.TFrame_functions.place(relx=0.007, rely=0.759, relheight=0.226
                , relwidth=0.456)
        self.TFrame_functions.configure(relief='groove', borderwidth="2")

        self.Labelframe_key = tk.LabelFrame(self.TFrame_functions)
        self.Labelframe_key.place(relx=0.015, rely=0.065, relheight=0.484
                , relwidth=0.222)
        self.Labelframe_key.configure(relief='groove', foreground="black", text='''Key''')

        self.TEntry_key = ttk.Entry(self.Labelframe_key)
        self.TEntry_key.place(relx=0.133, rely=0.4, relheight=0.347
                , relwidth=0.773, bordermode='ignore')
        self.TEntry_key.configure(takefocus="", cursor="ibeam")
        self.TEntry_key.insert(tk.INSERT,"0000")

        self.TButton_start = ttk.Button(self.TFrame_functions)
        self.TButton_start.place(relx=0.355, rely=0.161, height=50, width=118)
        self.TButton_start.configure(takefocus="", text='''START''', command = self.var_chioce)

        self.Labelframe_open_image = tk.LabelFrame(self.TFrame_functions)
        self.Labelframe_open_image.place(relx=0.695, rely=0.065, relheight=0.484, relwidth=0.222)
        self.Labelframe_open_image.configure(relief='groove', foreground="black", text='''Browse Image''')

        self.TButton_open_image = ttk.Button(self.Labelframe_open_image)
        self.TButton_open_image.place(relx=0.133, rely=0.4, height=30, width=101, bordermode='ignore')
        self.TButton_open_image.configure(takefocus="", text='''Open Image...''', command = self.FileDialogForInputImage)

        self.var_technique = tk.IntVar()
        self.style.map('TRadiobutton',background = [('selected', _bgcolor), ('active', _ana2color)])
        self.TRadiobutton_LSB = ttk.Radiobutton(self.TFrame_functions)
        self.TRadiobutton_LSB.place(relx=0.104, rely=0.71, relwidth=0.297, relheight=0.0, height=26)
        self.TRadiobutton_LSB.configure(variable=self.var_technique, text='''LSB(Lowest Significant Bit)''', value = 1)

        self.TRadiobutton_BPCS = ttk.Radiobutton(self.TFrame_functions)
        self.TRadiobutton_BPCS.place(relx=0.518, rely=0.71, relwidth=0.459, relheight=0.0, height=26)
        self.TRadiobutton_BPCS.configure(variable=self.var_technique, text='''BPCS(Bit-Plane Complexity Segmentation)''', value = 2)

        self.Scrolledtext_message = ScrolledText(self.TFrame_main)
        self.Scrolledtext_message.place(relx=0.472, rely=0.088, relheight=0.902, relwidth=0.526)
        self.Scrolledtext_message.configure(background="white", font="TkTextFont", foreground="black", highlightbackground="#d9d9d9", highlightcolor="black")
        self.Scrolledtext_message.configure(insertbackground="black", insertborderwidth="3", selectbackground="#c4c4c4", selectforeground="black", wrap="none")

        self.TLabel_message = ttk.Label(self.TFrame_main)
        self.TLabel_message.place(relx=0.66, rely=0.015, height=44, width=177)
        self.TLabel_message.configure(foreground="#000000", font=font14, relief="flat", anchor='w', justify='left',text='''Secret Message''')

        self.top.mainloop()

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')