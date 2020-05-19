"""
   *Face Tracking System Using Arduino - Python Code*
    Close the Arduino IDE before running this code to avoid Serial conflicts.
    Replace 'COM5' with the name of port where you arduino is connected.
    To find the port check Arduino IDE >> Tools >> port.
    Upload the Arduino code before executing this code.

    # Code by Harsh Dethe, 09 Sep 2018 #
"""
import numpy as np
import serial
import time
import sys
import cv2
time.sleep(2)
print("Connection to arduino...")
tim=0
li=[]
li2=[]
ti=[]

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture('test4.mp4')

while 1:
    ret, img = cap.read()
    cv2.resizeWindow('img', 500,500)
    cv2.line(img,(500,250),(0,250),(0,255,0),1)
    cv2.line(img,(250,0),(250,500),(0,255,0),1)
    cv2.circle(img, (250, 250), 5, (255, 255, 255), -1)
    gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3)
    cv2.imshow("feed", img)
    ti.append(time.time())

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
        roi_gray  = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        arr = {y:y+h, x:x+w}
        print (arr)
        
        print ('X :' +str(x))
        print ('Y :'+str(y))
        print ('x+w :' +str(x+w))
        print ('y+h :' +str(y+h))

        xx = int(x+(x+h))/2
        yy = int(y+(y+w))/2
        li.append(xx)
        li2.append(yy)

        print (xx)
        print (yy)

        center = (xx,yy)

        print("Center of Rectangle is :", center)
        data = "X{0:f}Y{1:f}Z".format(xx, yy)
        print ("output = '" +data+ "'")
       
    
    
        
    cv2.imshow('img',img)
    
    k = cv2.waitKey(30) & 0xff
    
    if k == 27:
        dis=dis=(((li[0]-li2[0]**2)+(li2[-1]-li2[-1]**2)+(2400*2400))**.5)*0.00394
        time=ti[-1]-ti[0]
        print(time)
        print(dis)
        break
