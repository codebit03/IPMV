#power transform
import cv2
import numpy as np
import matplotlib.pyplot as plt
abc=cv2.imread ("D:/image1.jpeg",0)
plt.subplot (1,3,1)
plt.title ("original image")
plt.imshow (abc,cmap='gray')
xyz=np.array(255*(abc/255)**0.2,dtype='uint8')
plt.subplot(1,3,2)
plt.title("gamma<1")
plt.imshow(xyz,cmap='gray')
xyz=np.array(255*(abc/255)**3,dtype='uint8')
plt.subplot(1,3,3)
plt.title("gamma>1")
plt.imshow(xyz,cmap='gray')
plt.show()
