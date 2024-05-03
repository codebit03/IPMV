import cv2
abc=cv2.imread("D:/image1.jpeg",0)
print(abc)
cv2.imshow('original image',abc)
xyz=255-abc
xyz=~abc
xyz=cv2.bitwise_not(abc)
cv2.imshow('negated image',xyz)
