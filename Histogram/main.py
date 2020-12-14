import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('digitalimage.jpg')
color = ('b','g','r')

# plt.imshow(img, interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()

for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()