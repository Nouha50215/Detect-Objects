# Object Detection in Python (SPP-- Using ML and OpenCV)

# Load the image 
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("image.jpg") #Reads the image.


# Converting Image Color Formats
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Convert BGR to RGB and BGR to grayscale/ from one color space to another 
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(img_rgb) # Displays the image in a Matplotlib window. 
plt.show() # Renders the image.



