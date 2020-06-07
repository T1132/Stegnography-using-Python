import sys
import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from encoder_bpcs import Encoder_bpcs
from encoder_LSB import Encoder_LSB
import matplotlib.pyplot as plt
import cv2

class ENCODER:

    def histogram_input_image(self):

        img = Image.open(self.imagefilename)

        r, g, b = img.split()

        r_histo = r.histogram()
        g_histo = g.histogram()
        b_histo = b.histogram()

        fig = plt.gcf()
        DPI = fig.get_dpi()
        fig.set_size_inches(435.0/float(DPI),195.0/float(DPI))

        fig = plt.plot(r_histo, color = 'red')
        fig = plt.plot(g_histo, color = 'green')
        fig = plt.plot(b_histo, color = 'blue')
        fig = plt.axis('off')

        newfilename = ''
        sub = ''
        for m in range(len(self.imagefilename)):
            if self.imagefilename[m] == '.' and self.imagefilename[m+1:len(self.imagefilename)] == 'png':
                newfilename = sub + "_histogram.png"
                break
            else:
                sub += self.imagefilename[m]

        plt.savefig(newfilename)

        img_input_histogram = Image.open(newfilename) 
        newsize = (435, 195) 
        img_input_histogram_resize = img_input_histogram.resize(newsize)  
        self.Canvas_histo_in.image = ImageTk.PhotoImage(img_input_histogram_resize)
        self.Canvas_histo_in.create_image(0, 0, image = self.Canvas_histo_in.image, anchor = 'nw')


    def histogram_output_image(self):

	    img = Image.open(self.steganoimagefilename)

	    r, g, b = img.split()

	    r_histo = r.histogram()
	    g_histo = g.histogram()
	    b_histo = b.histogram()

	    fig = plt.gcf()
	    DPI = fig.get_dpi()
	    fig.set_size_inches(435.0/float(DPI),195.0/float(DPI))

	    fig = plt.plot(r_histo, color = 'red')
	    fig = plt.plot(g_histo, color = 'green')
	    fig = plt.plot(b_histo, color = 'blue')
	    fig = plt.axis('off')

	    newfilename = ''
	    sub = ''
	    for m in range(len(self.steganoimagefilename)):
	    	if self.steganoimagefilename[m] == '.' and self.steganoimagefilename[m+1:len(self.steganoimagefilename)] == 'png':
	    		newfilename = sub + "_histogram.png"
	    		break
	    	else:
	    		sub += self.steganoimagefilename[m]

	    plt.savefig(newfilename)

	    img_output_histogram = Image.open(newfilename) 
	    newsize = (435, 195) 
	    img_output_histogram_resize = img_output_histogram.resize(newsize)  
	    self.Canvas_histo_out.image = ImageTk.PhotoImage(img_output_histogram_resize)
	    self.Canvas_histo_out.create_image(0, 0, image = self.Canvas_histo_out.image, anchor = 'nw')

    def var_chioce(self):
        self.choice = self.var_technique.get()
        if self.choice == 1:
            self.exploit_for_LSB()
        elif self.choice == 2:
            self.exploit_for_BPCS()

    def exploit_for_BPCS(self):

        self.steganoimagefilename = Encoder_bpcs.encoder_module(Encoder_bpcs,self.imagefilename, self.input_image_width, self.input_image_height
        , self.Scrolledtext_secretmsg.get("1.0", tk.END),self.Entry_key.get())

        self.histogram_output_image()

        self.FileDialogForOutputImage()
    
    def exploit_for_LSB(self):
    
        self.steganoimagefilename = Encoder_LSB.encoder_module(Encoder_LSB,self.imagefilename, self.input_image_width, self.input_image_height
        , self.Scrolledtext_secretmsg.get("1.0", tk.END),self.Entry_key.get())

        self.FileDialogForOutputImage()

        self.histogram_output_image()

    def FileDialogForOutputImage(self):

        self.img_output = Image.open(self.steganoimagefilename) 
        newsize = (369, 312) 
        self.img_output_resize = self.img_output.resize(newsize)  
        self.Canvas_output.image = ImageTk.PhotoImage(self.img_output_resize)
        self.Canvas_output.create_image(0, 0, image = self.Canvas_output.image, anchor = 'nw')

        self.output_image_size =  os.stat(self.steganoimagefilename).st_size
        self.Label_out_size1.configure(text = str(self.output_image_size)+" bytes")

        self.output_image_width, self.output_image_height = self.img_output.size
        self.Label_out_width1.configure(text = str(self.output_image_width)+" pixels")
        self.Label_out_height1.configure(text = str(self.output_image_height)+" pixels")

        img_original = cv2.imread(self.imagefilename)
        img_stegano = cv2.imread(self.steganoimagefilename)
        psnr = cv2.PSNR(img_original,img_stegano)
        psnr = float("{:.2f}".format(psnr))
        self.Label_out_psnr1.configure(text = str(str(psnr) +" db"))

    def FileDialogForInputImage(self):
    
        self.imagefilename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =(("png files","*.png"),("All files","*")))
        
        self.img_input = Image.open(self.imagefilename) 
        newsize = (369, 312) 
        self.img_input_resize = self.img_input.resize(newsize)  
        self.Canvas_input.image = ImageTk.PhotoImage(self.img_input_resize)
        self.Canvas_input.create_image(0, 0, image = self.Canvas_input.image, anchor = 'nw')

        self.histogram_input_image()

        self.input_image_size =  os.stat(self.imagefilename).st_size
        self.Label_in_size1.configure(text = str(self.input_image_size)+" bytes")

        self.input_image_width, self.input_image_height = self.img_input.size
        self.Label_in_width1.configure(text = str(self.input_image_width)+" pixels")
        self.Label_in_height1.configure(text = str(self.input_image_height)+" pixels")
        
        img_original = cv2.imread(self.imagefilename)
        psnr = cv2.PSNR(img_original,img_original)
        psnr = float("{:.2f}".format(psnr))
        self.Label_in_psnr1.configure(text = str(str(psnr) +" db"))
    
    def FileDialogForInputText(self):
        
        self.textfilename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =(("text files","*.txt"),("All files","*")))

        self.textfile = open(self.textfilename,'r')
        self.secret_msg = ''
        for line in self.textfile.readlines():
            self.secret_msg = self.secret_msg + str(line)
        self.Scrolledtext_secretmsg.insert(tk.INSERT,self.secret_msg)

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
        font9 = "-family {@Yu Gothic UI Semibold} -size 13 -weight "  \
            "bold"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        self.top.geometry("1500x700+0+0")
        self.top.minsize(148, 1)
        self.top.maxsize(1924, 1055)
        self.top.resizable(0, 0)
        self.top.title("Encoder")
        self.top.configure(background="#d9d9d9")

        self.main_frame = tk.Frame(self.top)
        self.main_frame.place(relx=0.007, rely=0.014, relheight=0.98
                , relwidth=0.991)
        self.main_frame.configure(relief='groove', borderwidth="2", background="#d9d9d9")
        
        self.TSeparator1 = ttk.Separator(self.main_frame)
        self.TSeparator1.place(relx=0.013, rely=0.625, relwidth=0.972)

        self.TSeparator2 = ttk.Separator(self.main_frame)
        self.TSeparator2.place(relx=0.639, rely=0.017, relheight=0.596)
        self.TSeparator2.configure(orient="vertical")

        self.Frame_input = tk.Frame(self.main_frame)
        self.Frame_input.place(relx=0.022, rely=0.034, relheight=0.566
                , relwidth=0.28)
        self.Frame_input.configure(relief='groove', borderwidth="2",background="#d9d9d9")

        self.Label_input = tk.Label(self.Frame_input)
        self.Label_input.place(relx=0.18, rely=0.021, height=28, width=251)
        self.Label_input.configure(background="#d9d9d9", disabledforeground="#a3a3a3", font=font9, foreground="#000000", text='''INPUT''')

        self.TSeparator3 = ttk.Separator(self.Frame_input)
        self.TSeparator3.place(relx=0.034, rely=0.116, relwidth=0.933)

        self.Canvas_input = tk.Canvas(self.Frame_input)
        self.Canvas_input.place(relx=0.06, rely=0.16, relheight=0.807
                , relwidth=0.887)
        self.Canvas_input.configure(background="#d9d9d9", borderwidth="2", insertbackground="black", relief="ridge", selectbackground="#c4c4c4")
        self.Canvas_input.configure(selectforeground="black")

        self.Frame_output = tk.Frame(self.main_frame)
        self.Frame_output.place(relx=0.336, rely=0.034, relheight=0.566
                , relwidth=0.28)
        self.Frame_output.configure(relief='groove', borderwidth="2", background="#d9d9d9")

        self.Label_output = tk.Label(self.Frame_output)
        self.Label_output.place(relx=0.2, rely=0.021, height=28, width=235)
        self.Label_output.configure(background="#d9d9d9", disabledforeground="#a3a3a3", font=font9, foreground="#000000", text='''OUTPUT''')

        self.TSeparator4 = ttk.Separator(self.Frame_output)
        self.TSeparator4.place(relx=0.031, rely=0.116, relwidth=0.938)

        self.Canvas_output = tk.Canvas(self.Frame_output)
        self.Canvas_output.place(relx=0.06, rely=0.16, relheight=0.807
                , relwidth=0.887)
        self.Canvas_output.configure(background="#d9d9d9", borderwidth="2", cursor="fleur", insertbackground="black", relief="ridge")
        self.Canvas_output.configure(selectbackground="#c4c4c4", selectforeground="#000000")

        self.TSeparator5 = ttk.Separator(self.main_frame)
        self.TSeparator5.place(relx=0.639, rely=0.643, relheight=0.344)
        self.TSeparator5.configure(orient="vertical")

        self.TSeparator6 = ttk.Separator(self.main_frame)
        self.TSeparator6.place(relx=0.316, rely=0.641, relheight=0.337)
        self.TSeparator6.configure(orient="vertical")

        self.Frame_histo_in = tk.Frame(self.main_frame)
        self.Frame_histo_in.place(relx=0.006, rely=0.644, relheight=0.341, relwidth=0.305)
        self.Frame_histo_in.configure(relief='groove', borderwidth="2", background="#d9d9d9")

        self.Label_histo_in = tk.Label(self.Frame_histo_in)
        self.Label_histo_in.place(relx=0.183, rely=0.034, height=21, width=269)
        self.Label_histo_in.configure(background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000", text='''Histogram Input Image''')

        self.Canvas_histo_in = tk.Canvas(self.Frame_histo_in)
        self.Canvas_histo_in.place(relx=0.018, rely=0.132, relheight=0.833, relwidth=0.96)
        self.Canvas_histo_in.configure(background="#d9d9d9", borderwidth="2", insertbackground="black", relief="ridge")
        self.Canvas_histo_in.configure(selectbackground="#c4c4c4", selectforeground="black")

        self.Frame_histo_out = tk.Frame(self.main_frame)
        self.Frame_histo_out.place(relx=0.325, rely=0.644, relheight=0.341, relwidth=0.305)
        self.Frame_histo_out.configure(relief='groove', borderwidth="2", background="#d9d9d9")

        self.Label_histo_out = tk.Label(self.Frame_histo_out)
        self.Label_histo_out.place(relx=0.148, rely=0.034, height=20, width=309)
        self.Label_histo_out.configure(background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000", text='''Histogram Output Image''')

        self.Canvas_histo_out = tk.Canvas(self.Frame_histo_out)
        self.Canvas_histo_out.place(relx=0.018, rely=0.132, relheight=0.833, relwidth=0.96)
        self.Canvas_histo_out.configure(background="#d9d9d9",borderwidth="2", insertbackground="black", relief="ridge",selectbackground="#c4c4c4")
        self.Canvas_histo_out.configure(selectforeground="black")

        self.Frame_info = tk.Frame(self.main_frame)
        self.Frame_info.place(relx=0.646, rely=0.015, relheight=0.592, relwidth=0.346)
        self.Frame_info.configure(relief='groove', borderwidth="2", background="#d9d9d9")

        self.var_technique = tk.IntVar()
        self.var_technique.set(1)
        self.R1 = tk.Radiobutton(self.top, text="LSB(Lowest Significant Bit)", variable=self.var_technique, value=1, command= "")
        self.R1.place(relx=0.680, rely=0.560, relwidth=0.110, relheight=0.0, height = 22)

        self.R2 = tk.Radiobutton(self.top, text="BPCS(Bit-Plane Complexity Segmentation)", variable=self.var_technique, value=2, command= "")
        self.R2.place(relx=0.800, rely=0.560, relheight=0.0, relwidth=0.165, height = 22)

        self.Labelframe_openimage = tk.LabelFrame(self.Frame_info)
        self.Labelframe_openimage.place(relx=0.01, rely=0.012, relheight=0.185, relwidth=0.292)
        self.Labelframe_openimage.configure(relief='groove', foreground="black", text='''Open Image''', background="#d9d9d9")

        self.Button_openimage = tk.Button(self.Labelframe_openimage)
        self.Button_openimage.place(relx=0.067, rely=0.4, height=33, width=130, bordermode='ignore')
        self.Button_openimage.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9", disabledforeground="#a3a3a3")
        self.Button_openimage.configure(foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", pady="0")
        self.Button_openimage.configure(text='''Choose An Image...''', command = self.FileDialogForInputImage)
        
        self.Button_start = tk.Button(self.Frame_info)
        self.Button_start.place(relx=0.331, rely=0.766, height=43, width=146)
        self.Button_start.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9", disabledforeground="#a3a3a3")
        self.Button_start.configure(font=font10, foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", pady="0")
        self.Button_start.configure(text='''START''', command = self.var_chioce)

        self.Scrolledtext_secretmsg = ScrolledText(self.Frame_info)
        self.Scrolledtext_secretmsg.place(relx=0.021, rely=0.271, relheight=0.463, relwidth=0.951)
        self.Scrolledtext_secretmsg.configure(background="white", font="TkTextFont", foreground="black", highlightbackground="#d9d9d9", highlightcolor="black")
        self.Scrolledtext_secretmsg.configure(insertbackground="black", insertborderwidth="3", selectbackground="#c4c4c4", selectforeground="black", wrap="none")

        self.Labelframe_key = tk.LabelFrame(self.Frame_info)
        self.Labelframe_key.place(relx=0.642, rely=0.012, relheight=0.182, relwidth=0.292)
        self.Labelframe_key.configure(relief='groove', foreground="black", text='''Enter Key''', background="#d9d9d9")

        self.Entry_key = tk.Entry(self.Labelframe_key)
        self.Entry_key.place(relx=0.067, rely=0.405, height=30, relwidth=0.867, bordermode='ignore')
        self.Entry_key.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont", foreground="#000000", insertbackground="black")
        self.Entry_key.insert(tk.INSERT,"0000")

        self.Labelframe_opentext = tk.LabelFrame(self.main_frame)
        self.Labelframe_opentext.place(relx=0.76, rely=0.022, relheight=0.108, relwidth=0.102)
        self.Labelframe_opentext.configure(relief='groove', foreground="black", text='''Open Text''', background="#d9d9d9")
        self.Labelframe_opentext.configure(highlightbackground="#d9d9d9", highlightcolor="black")

        self.Button_opentext = tk.Button(self.Labelframe_opentext)
        self.Button_opentext.place(relx=0.066, rely=0.405, height=33, width=130, bordermode='ignore')
        self.Button_opentext.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9", disabledforeground="#a3a3a3")
        self.Button_opentext.configure(foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Choose Text File...''')
        self.Button_opentext.configure(command = self.FileDialogForInputText)

        self.Frame1 = tk.Frame(self.main_frame)
        self.Frame1.place(relx=0.646, rely=0.641, relheight=0.343, relwidth=0.347)
        self.Frame1.configure(relief='groove', borderwidth="2", background="#d9d9d9")

        self.Frame_input_property = tk.Frame(self.Frame1)
        self.Frame_input_property.place(relx=0.019, rely=0.043, relheight=0.915, relwidth=0.475)
        self.Frame_input_property.configure(relief='groove', borderwidth="2", background="#d9d9d9")

        self.Label_input_property = tk.Label(self.Frame_input_property)
        self.Label_input_property.place(relx=0.204, rely=0.047, height=26, width=142)
        self.Label_input_property.configure(background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000", text='''Input Image''')

        self.Label_in_size = tk.Label(self.Frame_input_property)
        self.Label_in_size.place(relx=0.041, rely=0.186, height=36, width=52)
        self.Label_in_size.configure(background="#d9d9d9", disabledforeground="#a3a3a3", font=font10, foreground="#000000", text='''SIZE''')

        self.Label_in_psnr = tk.Label(self.Frame_input_property)
        self.Label_in_psnr.place(relx=0.041, rely=0.372, height=36, width=62)
        self.Label_in_psnr.configure(background="#d9d9d9", disabledforeground="#a3a3a3", font=font10, foreground="#000000", text='''PSNR''')

        self.Label_in_width = tk.Label(self.Frame_input_property)
        self.Label_in_width.place(relx=0.041, rely=0.605, height=26, width=72)
        self.Label_in_width.configure(background="#d9d9d9", disabledforeground="#a3a3a3", font=font10, foreground="#000000", text='''WIDTH''')

        self.Label__in_height = tk.Label(self.Frame_input_property)
        self.Label__in_height.place(relx=0.041, rely=0.791, height=26, width=82)
        self.Label__in_height.configure(background="#d9d9d9", disabledforeground="#a3a3a3", font=font10, foreground="#000000", text='''HEIGHT''')

        self.Label_in_size1 = tk.Label(self.Frame_input_property)
        self.Label_in_size1.place(relx=0.408, rely=0.209, height=26, width=72)
        self.Label_in_size1.configure(background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000")

        self.Label_in_psnr1 = tk.Label(self.Frame_input_property)
        self.Label_in_psnr1.place(relx=0.408, rely=0.395, height=26, width=72)
        self.Label_in_psnr1.configure(activebackground="#f9f9f9", foreground="#000000", background="#d9d9d9", disabledforeground="#a3a3a3")
        self.Label_in_psnr1.configure(foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black")

        self.Label_in_width1 = tk.Label(self.Frame_input_property)
        self.Label_in_width1.place(relx=0.408, rely=0.614, height=26, width=72)
        self.Label_in_width1.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9", disabledforeground="#a3a3a3")
        self.Label_in_width1.configure(foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black")

        self.Label_in_height1 = tk.Label(self.Frame_input_property)
        self.Label_in_height1.place(relx=0.408, rely=0.8, height=26, width=72)
        self.Label_in_height1.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9", disabledforeground="#a3a3a3")
        self.Label_in_height1.configure(foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black")

        self.Frame_output_property = tk.Frame(self.Frame1)
        self.Frame_output_property.place(relx=0.504, rely=0.043, relheight=0.915, relwidth=0.475)
        self.Frame_output_property.configure(relief='groove', borderwidth="2", background="#d9d9d9")

        self.Label_output_property = tk.Label(self.Frame_output_property)
        self.Label_output_property.place(relx=0.163, rely=0.047, height=26, width=158)
        self.Label_output_property.configure(background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000", text='''Output Image''')

        self.Label_out_size = tk.Label(self.Frame_output_property)
        self.Label_out_size.place(relx=0.041, rely=0.186, height=36, width=52)
        self.Label_out_size.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9", disabledforeground="#a3a3a3", foreground="#000000")
        self.Label_out_size.configure(font="-family {Segoe UI} -size 12", highlightbackground="#d9d9d9", highlightcolor="black", text='''SIZE''')

        self.Label_out_psnr = tk.Label(self.Frame_output_property)
        self.Label_out_psnr.place(relx=0.041, rely=0.372, height=36, width=62)
        self.Label_out_psnr.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9", disabledforeground="#a3a3a3")
        self.Label_out_psnr.configure(font="-family {Segoe UI} -size 12", foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", text='''PSNR''')

        self.Label_out_width = tk.Label(self.Frame_output_property)
        self.Label_out_width.place(relx=0.041, rely=0.605, height=26, width=72)
        self.Label_out_width.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9", disabledforeground="#a3a3a3")
        self.Label_out_width.configure(font="-family {Segoe UI} -size 12", foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", text='''WIDTH''')

        self.Label__out_height = tk.Label(self.Frame_output_property)
        self.Label__out_height.place(relx=0.041, rely=0.791, height=26, width=82)

        self.Label__out_height.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9", disabledforeground="#a3a3a3")
        self.Label__out_height.configure(font="-family {Segoe UI} -size 12", foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", text='''HEIGHT''')

        self.Label_out_size1 = tk.Label(self.Frame_output_property)
        self.Label_out_size1.place(relx=0.408, rely=0.219, height=26, width=72)
        self.Label_out_size1.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9", disabledforeground="#a3a3a3")
        self.Label_out_size1.configure(foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black")

        self.Label_out_psnr1 = tk.Label(self.Frame_output_property)
        self.Label_out_psnr1.place(relx=0.408, rely=0.405, height=26, width=72)
        self.Label_out_psnr1.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9", disabledforeground="#a3a3a3")
        self.Label_out_psnr1.configure(foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black")

        self.Label_out_width1 = tk.Label(self.Frame_output_property)
        self.Label_out_width1.place(relx=0.408, rely=0.609, height=26, width=72)
        self.Label_out_width1.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9", disabledforeground="#a3a3a3")
        self.Label_out_width1.configure(foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black")

        self.Label_out_height1 = tk.Label(self.Frame_output_property)
        self.Label_out_height1.place(relx=0.408, rely=0.8, height=26, width=72)
        self.Label_out_height1.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9", disabledforeground="#a3a3a3")
        self.Label_out_height1.configure(foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black")

        self.menubar = tk.Menu(self.top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        self.top.configure(menu = self.menubar)
        
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
