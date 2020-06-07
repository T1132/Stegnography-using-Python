# Importing Packages
import numpy as np # For Mathematical funnctions.
import cv2 # OpenCV.
from tkinter import Tk # for GUI Toolkit.
from tkinter import ttk # for Advanced Toolkt.
from perform_fun import perform # Self created package for common functions.

class Decoder_BPCS:

    #decoder module
    def decoder_module(self, imagefilename, width , height, key):
        stegano_image = cv2.imread(imagefilename)
        
        ct_indic = 0
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
        TProgressbar1['maximum'] = 3*3*height

        sub_img = np.zeros((height,width,1),np.uint8)

        bin_data = ''
        data = ''

        for color in range(3):
            
            for m in range(height):
                for n in range(width):

                    b,g,r = stegano_image[m,n]
                    
                    if color == 0:
                        sub_img[m,n] = b
                        
                    elif color == 1:
                        sub_img[m,n] = g
                        
                    elif color == 2:
                        sub_img[m,n] = r

            meta_loc = 0
            meta_data = ''
            for indic in range(5,8):
                
                patched_loc = ''
                meta_data = ''
                patched_indic = 0

                mean1 = 0.0
                std1 = 0.0
                patched_loc = ''
                patch_loc_len = 0
                
                bt = np.zeros((height,width,1),np.uint8)
                for m in range(height):
                    for n in range(width):
                        shape = str(perform.dec2bin(self,sub_img[m,n]))
                        if indic > 4:
                            bt[m,n] = int(shape[indic])
                        else:
                            break
                
                if indic > 4:
                    
                    if (height-(int(height/8)*8)) >= 4:
                        meta_loc = (int(height/8)*8)
                        
                    elif (height-(int(height/8)*8)) < 4:
                        meta_loc = (int(height/8)*8) - 8
                    
                    bt_str = ''
                    for m in range(meta_loc+1,height):
                        for n in range(width):
                            bt_str = bt_str + str(int(bt[m,n]))
                            
                    ct = 0
                    for n in range(0,len(bt_str),8):
                        tmp_bt = ''
                        for a in range(n,n+8):
                            tmp_bt  = tmp_bt + bt_str[a]
                                    
                        if str(chr(int(perform.bin2dec(self,int(tmp_bt))))) == ' ':
                            
                            if ct == 0:
                                if meta_data != str(meta_loc):
                                    break
                            
                            elif ct == 1:
                                mean1 = float(meta_data)

                            elif ct == 2:
                                std1 = float(meta_data)
                            
                            elif ct == 3:
                                patch_len = int(meta_data)
                             
                            elif ct == 4:
                                patched_loc = meta_data
                                
                            elif ct == 5:
                                patch_loc_len = int(meta_data)
                                
                            else:
                                break
                            
                            ct = ct + 1
                            meta_data = ""
                            
                        else:
                            meta_data = meta_data + str(chr(int(perform.bin2dec(self,int(tmp_bt)))))
                                
                    
                    tmp_patched_loc = ''
                    sub_str = ''   
                    
                    for a in range(len(patched_loc)):
                        
                        if patched_loc[a] == '@':
                            
                            tmp_patched_loc = tmp_patched_loc + str(perform.dec2bin(self,int(sub_str)))
                            sub_str = ''
                            
                        else:
                            
                            sub_str = sub_str + patched_loc[a]
                    
                        
                    patched_loc = tmp_patched_loc[0:patch_loc_len]
                    
                    if len(patched_loc) != 0:
                        for m in range(0,meta_loc,8):
                            for n in range(0,int(width/8)*8,8):
                                if patched_indic < patch_loc_len:
                                    
                                    oalpha = perform.alpha1(self,8,8,bt[m:m+8,n:n+8])

                                    if oalpha > (mean1-0*std1):
                                        
                                        if patched_loc[patched_indic] == "1":

                                            b_con = perform.conjugate(self,8,8,bt[m:m+8,n:n+8]) 
                                            bin_data = bin_data + perform.ext_data(self,8,8,b_con)  

                                        elif patched_loc[patched_indic] == "0":

                                            bin_data = bin_data + perform.ext_data(self,8,8,bt[m:m+8,n:n+8])

                                        patched_indic = patched_indic + 1
                            TProgressbar1['value'] = ct_indic
                            TProgressbar1.update()
                            ct_indic += 8
        data = ''
        sum1 = 0
        for i in range(len(key)):
            sum1 = sum1 + ord(key[i])
        key = str(perform.dec2bin(self,sum1))

        for m in range(0,len(bin_data),8):
            data = data + str(chr(int(perform.bin2dec(self,perform.XOR(self,bin_data[m:m+8],str(key))))))

        TProgressbar1['value'] = 3*3*height
        TProgressbar1.update()
        progress_window.destroy()

        return data