import cv2
import numpy as np
import matplotlib.pyplot as plt

abc=cv2.imread ("D:/image1.jpeg",0)
plt.subplot(2,2,1)
plt.title("Original image")
plt.imshow(abc,cmap='gray')
hedf_mask=np.array([[-1,-1,-1],[2,2,2],[-1,-1,-1]])
hed_image=cv2.filter2D(abc,-1,hedf_mask)
plt.subplot(2,2,2)
plt.title("HED image")
plt.imshow(hed_image,cmap='gray')
plt.show()
