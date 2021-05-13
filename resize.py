import  cv2
import numpy

def resize(img):
 width=256
 height=256
 dim=(256,256)
 #resizing the images to 256 X 256 pixels
 resized=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
 #pasting the resized image to the folder in the path provided
 return(resized)