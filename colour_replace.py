import cv2
import numpy as np
from matplotlib import pyplot as plt
from colour_convert import convert
from notification import mail

def mask(img):
    img_rgb, img_hsv = convert(img)

    #Set range for colour detection
    light_grey = (0, 0, 160)
    dark_grey = (175, 50, 250)

    mask = cv2.inRange(img_hsv, light_grey, dark_grey) #Generate mask to isolate smoke
    result = cv2.bitwise_and(img_rgb, img_rgb, mask=mask) #Apply mask to image
    blur = cv2.GaussianBlur(result, (7, 7), 0) #apply gaussian filter to remove noise from image
    shape = blur.shape
    notBlack = np.where(blur != [0,0,0]) #Generate array of all non black pixels
    return shape, notBlack

def main(image):
    shape, notBlack = mask(image)
    meanx = np.mean(notBlack[1]) #Compute the average x-value of the smoke
    meany = np.mean(notBlack[0]) #Compute the average y-value of the smoke

    #Check which direction the smoke is traveling
    third01 = int(shape[0]/4)
    third02 = int(2*shape[0]/3)
    third11 = int(shape[1]/3)
    third12 = int(2*shape[1]/3)

    print(meanx, meany)

    if meanx > shape[1]/2:
        d1 = "East"
    else:
        d1 = "West"
    if meany > shape[0]/2:
        d2 = "South"
    else:
        d2 = "North"
    try:
        d
    except NameError:
        direction = d2+"-"+d1
    else:
        direction = d
    if direction != "-":
        print(direction)
        mail(direction)
