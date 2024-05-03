import cv2
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,svm,metrics
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
digits= datasets.load_digits()
print('keys of digits dataset:',digits.keys())
print('shape of data:',digits.data.shape)
print('data:',digits.data)
print('shape of target:',digits.target.shape)
print('target:',digits.target)
print('shape of images:',digits.images.shape)
for i in range (10):
    plt.subplot(2,5,i+1)
    plt.axis('off')
    plt.imshow(digits.images[i],cmap= 'gray_r')
    plt.title('target:{}'.format(digits.target[i]))
    
train_data,test_data,train_target,test_target=train_test_split(digits.data,digits.target,test_size=0.5,shuffle=True)
print('size of training data:',train_data.shape)
print('size of testing data:',test_data.shape)
print('size of training target:',train_target.shape)
print('size of testing target:',test_target.shape)
model_linear=svm.SVC(kernel='linear')
model_linear.fit(train_data,train_target)
predict=model_linear.predict(test_data)
acc = metrics.accuracy_score(test_target,predict)
print('accuracy = {}'.format(acc*100,'%'))
confusion_matrics= matrics = metrics.confusion_matrix(test_target,predict)
cm_display =metrics.ConfusionMatrixDisplay(confusion_matrics)
cm_display.plot()
plt.show()
for i in range (4):
    abc = np.reshape(test_data[i],(8,8))
    plt.subplot(2,2,i+1)
    plt.axis('off')
    plt.title('predicted:{}'.format(predict[i]))
    plt.imshow(abc,cmap ='gray_r')
plt.show()

