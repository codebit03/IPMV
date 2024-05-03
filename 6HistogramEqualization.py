#histogram

import cv2
import numpy as np
import matplotlib.pyplot as plt

abc=cv2.imread ("D:/image1.jpeg",0)
plt.subplot (2,2,1)
plt.title ("original image")
plt.imshow (abc,cmap='gray')
plt.subplot(2,2,2)
plt.title("histogram")
plt.xlim([0,256])
plt.ylim([0,12500])
plt.hist(abc.flatten(),256,[0,255],color='r')
xyz=cv2.equalizeHist(abc)
plt.subplot (2,2,3)
plt.title ("equalize")
plt.imshow (abc,cmap='gray')
plt.subplot(2,2,4)
plt.title("equalize histogram")
plt.xlim([0,256])
plt.ylim([0,12500])
plt.hist(xyz.flatten(),256,[0,255],color='g')
plt.show()
