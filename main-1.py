import UCIQE
import UIQM
import cv2
import numpy as np
import os
import glob
import openpyxl
import shutil
import haze
import resize
import with_exel


if __name__=="__main__":

 #insert the path of source file of the images
 source = (r"E:\college\dbms\data\EUVP Dataset\Paired\underwater_dark\trainA")

 # Insert path of the file in which you want the degraded images
 degraded = (r"C:\Users\hp\Desktop\DBMS_PROJECT\Dataset\EUVP Dataset\Paired\underwater_imagenet\degraded")

 #Insert the path to the file where you want clear images
 clear = (r"C:\Users\hp\Desktop\DBMS_PROJECT\Dataset\EUVP Dataset\Paired\underwater_imagenet\clear")
 

 #i= int(input("Please enter 1 if you want to enter the values in exel sheet : "))
 i=1  #(change the i value if want values in exel sheet)
 j=0
 
 if(i==1):
    #Insert the path of the exel sheet in which the values is to be pasted
    exel=(r"E:\college\dbms\data\EUVP Dataset\Paired\underwater_dark\new1.xlsx")
 
    j ,m_uism, m_uicm, m_uiqm = with_exel.sep(source,degraded,clear,exel, 2, 0.00, 0.00, 0.00)
    print(j)

 source = (r"E:\college\dbms\data\EUVP Dataset\Paired\underwater_dark\trainB")
   
 j,m_uism, m_uicm, m_uiqm = with_exel.sep(source,degraded,clear,exel , j,m_uism, m_uicm, m_uiqm)
 print(j)

 
 
 
 
 
 
 
 
 
 
 
 
 
 