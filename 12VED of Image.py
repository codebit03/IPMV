import cv2
import numpy as np
import matplotlib.pyplot as plt

abc=cv2.imread ("D:/image1.jpeg",0)
plt.subplot(2,2,1)
plt.title("Original image")
plt.imshow(abc,cmap='gray')
ved_mask=np.array([[-1,2,-1],[-1,2,-1],[-1,2,-1]])
ved_image=cv2.filter2D(abc,-1,ved_mask)
plt.subplot(2,2,3)
plt.title("VED image")
plt.imshow(ved_image,cmap='gray')
plt.show()
