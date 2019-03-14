import cv2
import numpy as np
from matplotlib import pyplot as plt
from colour_convert import convert
import colour_replace

def mask():
    img = cv2.imread('images/fire10.jpg',1)
    img_rgb,img_hsv = convert(img)
    lighter_red = (1,150,150)
    darker_red = (18,255,255)

    mask = cv2.inRange(img_hsv,lighter_red,darker_red)
    result = cv2.bitwise_and(img_rgb,img_rgb,mask=mask)

    return result, img

def main():
    res, img = mask()
    if not np.all(res == [0,0,0]):
        shape = res.shape
        red = np.where(res != [0,0,0])
        meanx = np.mean(red[1])
        meany = np.mean(red[0])

        y = meany - (shape[0]/2)
        if y<0:y=0
        x = meanx - (shape[1]/2)
        if x<0:x=0
        y1 = meany + (shape[0]/2)
        if y1 > shape[0]:y1=shape[0]
        x1 = meanx + (shape[1]/2)
        if x1 > shape[1]:x1=shape[1]
        crop_img = img[int(y):int(y1),int(x):int(x1)]
        colour_replace.main(crop_img)
    else:
        print("No fire detected")
if __name__=='__main__':
    main()
