import cv2
import numpy as np
import matplotlib.pyplot as plt
abc=cv2.imread ("D:/image1.jpeg",0)
plt.subplot(1,3,1)
plt.title("Original image")
plt.imshow(abc,cmap='gray')
hpf_mask=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
hp_image=cv2.filter2D(abc,-1,hpf_mask)
plt.subplot(1,3,2)
plt.title("HPF image")
plt.imshow(hp_image,cmap='gray')
plt.show()
