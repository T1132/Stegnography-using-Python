import numpy as np
import cv2

class perform:
    # Decimal to Binary convertor
    def dec2bin(self,dec):
        inverse = ''
        binary = ''
        while dec != 0:
            inverse = inverse + str( int(dec % 2) )
            dec = int(dec / 2)
        if len(inverse) <= 8:
            size = len(inverse)
            for i in range(8-size):
                inverse = inverse + '0'
        for i in range(len(inverse)-1,-1,-1):
            binary = binary + str(inverse[i])
        return binary

    # Binary to Decimal convertor
    def bin2dec(self,binar):
        binar = int(binar)
        dec = 0
        i = 0
        while binar > 0:
            dec = dec + (int(binar%10)*np.power(2,i))
            i = i+1
            binar = int(binar/10)
        return dec

    # XOR operation
    def XOR(self,data,key):
        data = str(data)
        
        key = str(key)
        
        enc_data = ''
        for ext_data in range(len(data)):
            if data[ext_data] == '0' and key[ext_data] == '0':
                enc_data = enc_data + '0'
            elif data[ext_data] == '0' and key[ext_data] == '1':
                enc_data = enc_data + '1'
            elif data[ext_data] == '1' and key[ext_data] == '0':
                enc_data = enc_data + '1'
            elif data[ext_data] == '1' and key[ext_data] == '1':
                enc_data = enc_data + '0'
        return enc_data

    # Secret Message into ASCII and ASCII into Binary format
    def get_cooked_data(self,secret_message, key):
        binary = ''
        count = 0
        tmp = ''
        if key.isnumeric() and (len(key) == 4):
            sum1 = 0
            for i in range(len(key)):
                sum1 = sum1 + ord(key[i])
            key = str(perform.dec2bin(perform,sum1))

            for pos in range(len(secret_message)):
                if ord(secret_message[pos]) <= 255:
                    if count < 8:
                        tmp = str(perform.XOR(perform,perform.dec2bin(perform,ord(secret_message[pos])),key))# coverting Secret code into ASCII and ASCII into Encrypted Binary.
                        binary = binary + tmp
                    else:
                        tmp = count = 0
            
            len_b = len(binary)
            if (len_b-(int(len_b/64)*64)) != 0:
                extra = len_b-(int(len_b/64)*64)
                for pos in range(64-extra):
                    binary = binary + '0'
                
            return binary
        else:
            exit()

    # XOR operation
    def XOR1(self, h,w,d1,d2):
        enc_data = np.zeros((h,w,1),np.uint8)
        for ext_data in range(h):
            for ext_dataj in range(w):
                if (int(d1[ext_data,ext_dataj]) == 0) and (int(d2[ext_data,ext_dataj]) == 0):
                    enc_data[ext_data,ext_dataj] =  0
                elif (int(d1[ext_data,ext_dataj]) == 0) and (int(d2[ext_data,ext_dataj]) == 1):
                    enc_data[ext_data,ext_dataj] =  1
                elif (int(d1[ext_data,ext_dataj]) == 1) and (int(d2[ext_data,ext_dataj]) == 0):
                    enc_data[ext_data,ext_dataj] =  1
                elif (int(d1[ext_data,ext_dataj]) == 1) and (int(d2[ext_data,ext_dataj]) == 1):
                    enc_data[ext_data,ext_dataj] =  0
        return enc_data

    # To calculate the complexity of a 8*8 block of binary image
    def alpha1(self, h,w,b):
        x = 0
        count = 0
        change = 0
        for j in range(h):
            for k in range(w):
                if j == 0 and k == 0:
                    count = 0
                    change = int(b[j,k])
                else:
                    if change != int(b[j,k]):
                        count = count + 1
                        change = int(b[j,k])
        x = count/(h*w-1)
        return x      

    # To conjugate a block of binary image
    def conjugate(self, h,w,b_ex):  
        wc = np.zeros((h,w,1),np.uint8)
        for i in range(8):
            for j in range(8):
                if int(j%2) != 0:
                    wc[i,j] = 1

        b_ex_tmp = perform.XOR1(perform,h,w,wc,b_ex)
        return b_ex_tmp

    # To extract the data from block of binary image to a string format
    def ext_data(self,h,w,d):
        tmp_data = ""
        for a in range(h):
            for b in range(w):
                tmp_data = tmp_data + str(int(d[a,b]))
        return tmp_data