import cv2
import matplotlib.pyplot as plt
import numpy as np
abc=cv2.imread ("D:/image1.jpeg",0)
plt.subplot(1,2,1)
plt.title ("Original image")
plt.imshow(abc,cmap='gray')
lpf_mask=np.ones((3,3))/9
lpf_image=cv2.filter2D(abc,-1,lpf_mask)
plt.subplot(1,2,2)
plt.title ("filter image")
plt.imshow(lpf_image,cmap='gray')
plt.show()
