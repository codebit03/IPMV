#Contrast image:
import cv2
import numpy as np
import matplotlib.pyplot as plt
abc=cv2.imread("C:/Users/saide/OneDrive/Desktop/prerana kadam/images/insect.jpg",0)
plt.subplot(1,3,1)
plt.title("Original image")
plt.imshow(abc,cmap="gray")
contrast=3
xyz=np.zeros(abc.shape,abc.dtype)
xyz=np.clip(contrast*abc,0,255)
plt.subplot(1,3,2)
plt.title("image 1")
plt.imshow(xyz,cmap="gray")
pqr=cv2.convertScaleAbs(abc,alpha=1.5,beta=10)
plt.subplot(1,3,3)
plt.title("image 2")
plt.imshow(pqr,cmap="gray")
plt.show()
