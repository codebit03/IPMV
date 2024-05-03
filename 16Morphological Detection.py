#Edge Detection or Boundry Detection

import cv2
import numpy as np
import matplotlib.pyplot as plt
abc=cv2.imread("D:\image1.jpeg",0)
print(abc)
plt.subplot(1,2,1)
plt.title("Original image")
plt.imshow(abc,cmap='gray')
strct=np.array([[255,0,255],[0,255,0],[255,0,255]],np.uint8)
img_erosion=cv2.erode(abc,strct, iterations=1)
xyz=abc-img_erosion
plt.subplot(1,2,2)
plt.title("new image")
plt.imshow(xyz,cmap="gray")
plt.show()

