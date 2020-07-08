# confess警告
# 数据集是gitbub上的

import cv2

path = "haarcascade_frontalcatface.xml"
faceCascade = cv2.CascadeClassifier(path)
img = cv2.imread("cat1.jpg")  
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = faceCascade.detectMultiScale(gray_img,scaleFactor=1.02,minNeighbors=3,minSize=(150, 150),flags=cv2.CASCADE_SCALE_IMAGE)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.putText(img,'Cat',(x,y-7), 3, 1.2, (0, 255, 0), 2, cv2.LINE_AA)

if (len(faces) != 0):
    cv2.imshow('output', img)
    cv2.imwrite("output.jpg",img)
    c = cv2.waitKey(0)
else:
    print("cat not found!")

