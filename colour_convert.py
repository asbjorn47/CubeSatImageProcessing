import cv2
def convert(image):
    img_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    img_hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    return img_rgb, img_hsv
