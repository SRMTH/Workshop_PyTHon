import cv2
import numpy
# read image
img = cv2.imread('logo.jpeg')
 
# apply guassian blur on src image
blurred = cv2.GaussianBlur(img,(7,7),2)
 
# display input and output image
cv2.imshow("Gaussian Smoothing",blurred)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
