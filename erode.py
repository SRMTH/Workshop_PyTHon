import cv2
import numpy as np
img = cv2.imread('logo.jpeg')
kernel = np.ones((5,5),np.uint8)                #kernel for ersion and dilation
erosion = cv2.erode(img,kernel,iterations = 2)  #opencv built-in function to erode an image  
cv2.imshow('erode',erosion)

dilation = cv2.dilate(img,kernel,iterations = 2) #opencv built-in function to dilate an image
cv2.imshow('dilate',dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
