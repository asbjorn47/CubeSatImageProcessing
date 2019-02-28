import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('fire2.jpg',1)
img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #Convert image to RGB colour space
img_hsv = cv2.cvtColor(img_rgb,cv2.COLOR_RGB2HSV) #Convert image to HSV color space

#Set range for colour detection
light_grey = (0, 0, 160)
dark_grey = (175, 50, 250)


mask = cv2.inRange(img_hsv, light_grey, dark_grey) #Generate mask to isolate smoke
result = cv2.bitwise_and(img_rgb, img_rgb, mask=mask) #Apply mask to image
blur = cv2.GaussianBlur(result, (7, 7), 0) #apply gaussian filter to remove noise from image

shape = blur.shape

notBlack = np.where(blur != [0,0,0]) #Generate array of all non black pixels
meanx = np.mean(notBlack[1]) #Compute the average x-value of the smoke
meany = np.mean(notBlack[0]) #Compute the average y-value of the smoke

#Check which direction the smoke is traveling
print("Diretion:")
if meanx > shape[1]/2:
    print("Right Side")
else:
    print("Left Side")
if meany > shape[0]/2:
    print("Bottom")
else:
    print("Top")
