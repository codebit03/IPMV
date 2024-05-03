import cv2
import numpy as np
import matplotlib.pyplot as plt

abc=cv2.imread ("D:/image1.jpeg",0)
plt.subplot(2,2,1)
plt.title("Original image")
plt.imshow(abc,cmap='gray')
ded_mask=np.array([[2,-1,-1],[-1,2,-1],[-1,-1,2]])
ded_image=cv2.filter2D(abc,-1,ded_mask)
plt.subplot(2,2,4)
plt.title("DED image")
plt.imshow(abc,cmap='gray')
           
