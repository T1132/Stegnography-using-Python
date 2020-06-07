# Importing Packages 
import numpy as np # For Mathematical funnctions.
import cv2 # OpenCV.
from tkinter import Tk # for GUI Toolkit.
from tkinter import ttk # for Advanced Toolkt.
from perform_fun import perform # Self created package for common functions.

class Encoder_LSB():
        
# Writing Changes to Cover Image and Generating a Steagnographed Image.
    def encoder_module(self, imagefilename, width , height, textfilename, key):

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

        img = cv2.imread(imagefilename)
        binary = perform.get_cooked_data(self,textfilename, key)
        len_binary = len(binary)
        k = 0
        stegano_img = img # Initializing the steagno image with original image.

        hidden = 0

        TProgressbar1['maximum'] = len_binary

        for i in range(height):

            for j in range(width):
                if k < len_binary: 
                    b,g,r = img[i,j] # blue, green , red values in a pixel.
                    bin_b = int(perform.dec2bin(self,b)) # binary form of blue pixel value.
                    bin_g = int(perform.dec2bin(self,g)) # binary form of green pixel value.
                    bin_r = int(perform.dec2bin(self,r)) # binary form of red pixel value.
                    
                    if k < len_binary:

                        if int(bin_b % 10) == int(binary[k]):
                            k = k+1

                        else:

                            if int(bin_b%10) == 0:
                                bin_b = (int(bin_b/10)*10) + 1

                            else:
                                bin_b = int(bin_b/10)*10

                            k = k+1
                            
                    if k < len_binary:

                        if int(bin_g % 10) == int(binary[k]):
                            k = k+1

                        else:

                            if int(bin_g%10) == 0:
                                bin_g = (int(bin_g/10)*10) + 1

                            else:
                                bin_g = int(bin_g/10)*10

                            k = k+1
                        
                    if k < len_binary:

                        if int(bin_r % 10) == int(binary[k]):
                            k = k+1

                        else:

                            if int(bin_r%10) == 0:
                                bin_r = (int(bin_r/10)*10) + 1

                            else:
                                bin_r = int(bin_r/10)*10

                            k = k+1
                    
                    # Updating the original Pixel values. 
                    b = np.uint8(perform.bin2dec(self,bin_b))
                    g = np.uint8(perform.bin2dec(self,bin_g))
                    r = np.uint8(perform.bin2dec(self,bin_r))
                    stegano_img[i,j] = [b,g,r]
                    hidden = hidden + 1 

                    TProgressbar1['value'] = k
                    TProgressbar1.update()    

                else:
                    break

        steagnoimagefilename = ''
        sub = ''
        for m in range(len(imagefilename)):
            if imagefilename[m] == '.' and imagefilename[m+1:len(imagefilename)] == 'png':
                steagnoimagefilename = sub + "_stegano_LSB.png"
                break
            else:
                sub += imagefilename[m]
        
        cv2.imwrite(steagnoimagefilename,stegano_img)
        progress_window.destroy()
        
        return steagnoimagefilename