#program for log transform
import cv2
import numpy as np
import matplotlib.pyplot as plt
abc=cv2.imread ("D:/image1.jpeg",0)
plt.subplot(1,2,1)
plt.title("original image")
plt.imshow(abc,cmap='gray')
c=255/np.log(1+np.max(abc))
xyz=np.zeros(abc.shape,abc.dtype)
for i in range(abc.shape[0]):
 for j in range(abc.shape[1]):
    xyz[i,j]=c*np.log(1+abc[i,j])
plt.subplot(1,2,2)
plt.title("log transform image")
plt.imshow(xyz,cmap='gray')
plt.show()
