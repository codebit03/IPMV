import cv2
import numpy as np
import matplotlib.pyplot as plt
abc=cv2.imread("D:/image1.jpeg",1)
abc= cv2.cvtColor(abc,cv2.COLOR_BGR2RGB)
plt.subplot(1,2,1)
plt.title('Original image')
plt.imshow(abc)
pixel_val=abc.reshape((-1,3))
pixel_val=np.float32(pixel_val)
k=4
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,100,0.85)
retval,labels,centers=cv2.kmeans(pixel_val,k, None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
#print('retval',retval)
#print('labels",labels)
#print('centers',centers)
centers= np.uint8(centers)
print('centers',centers)
segmented_data =centers[labels.flatten()]
print('segmented_data',segmented_data)
segmented_image =segmented_data.reshape(abc.shape)
plt.subplot(1,2,2)
plt.title('segmented_image')
plt.imshow(segmented_image)
plt.show()
