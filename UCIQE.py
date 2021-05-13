import cv2
import numpy as np

def chroma(image):

    (B, G, R) = cv2.split(image)

    #Chroma
    con=cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    (l,a,b)=cv2.split(con)
    chroma = np.sqrt(a**2 + b**2)

    u_c = np.mean(chroma)

    return( np.sqrt(np.mean(np.mean(chroma**2 - u_c**2))))
   #standard deviation of chorma

    #rg = np.absolute(0.439*R - 0.399*G -0.04*B + 128)

def luminance(image):
    #luminance -----calculate luminance using  Y=0.2126R+0.7152G+0.0722B
    con=cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    (l,a,b)=cv2.split(con)
    lmin=np.amin(l)
    lmax=np.amax(l)
    return((lmax-lmin))



def saturation(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)
    return(np.mean(s))



def ucique(image):
    c1 = 0.4680
    c2 = 0.2745
    c3 = 0.2576
    uciqe=c1*chroma(image) +c2*luminance(image) + c3*saturation(image)
    return (uciqe)