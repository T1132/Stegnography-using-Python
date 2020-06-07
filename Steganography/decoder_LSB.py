# Importing Packages 
import numpy as np # For Mathematical funnctions.
import cv2 # OpenCV.
from tkinter import Tk # for GUI Toolkit.
from tkinter import ttk # for Advanced Toolkt.
from perform_fun import perform # Self created package for common functions.

class Decoder_LSB:

    # Extracting the Secret Message for the Image.
    def decoder_module(self, imagefilename, width , height, key):
        steagno1_img = cv2.imread(imagefilename) # Reading an Steagnographed Image.

        progress_window = Tk()
        progress_window.geometry("646x67+685+189")
        progress_window.minsize(148, 1)
        progress_window.maxsize(1924, 1055)
        progress_window.resizable(0, 0)
        progress_window.title("Progress")
        progress_window.configure(background="#d9d9d9")

        TProgressbar1 = ttk.Progressbar(progress_window)
        TProgressbar1.place(relx=0.031, rely=0.194, relwidth=0.944
                , relheight=0.0, height=40)
        TProgressbar1.configure(length="610")
        TProgressbar1['maximum'] = height

        sum1 = 0
        for i in range(len(key)):
                sum1 = sum1 + ord(key[i])
        key = str(perform.dec2bin(self,sum1))
        extracted_code = ''
        
        for i in range(height):
            for j in range(width):
                b,g,r = steagno1_img[i,j] # blue, green , red values in a pixel.
                bin_b = int(perform.dec2bin(self,b)) # binary form of blue pixel value.
                bin_g = int(perform.dec2bin(self,g)) # binary form of green pixel value.
                bin_r = int(perform.dec2bin(self,r)) # binary form of red pixel value.
                extracted_code = extracted_code + str(int(bin_b%10)) + str(int(bin_g%10)) + str(int(bin_r%10))
            TProgressbar1['value'] = i
            TProgressbar1.update()

        word = ''
        for leng in range(0,len(extracted_code),8):
            word =  word + str(chr(perform.bin2dec(self,perform.XOR(self,extracted_code[leng:(leng+8)],key))))
        
        progress_window.destroy()

        return word