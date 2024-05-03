#thresholding of an image
import cv2
import numpy as np
abc=cv2.imread("D:/image1.jpeg",0)
cv2.imshow('original image',abc)
xyz=np.zeros(abc.shape,abc.dtype)
cv2.waitKey(0)
print("shape of image:",abc.shape)
#method 1
for i in range(490):
 for j in range(487):
  if (abc[i,j]<127):
     xyz[i,j]=0
  else:
    xyz[i,j]=255
cv2.imshow("new image",xyz)
