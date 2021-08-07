import cv2
import numpy as np
import face_recognition
import os
import csv
from datetime import datetime, date
import serial
import time

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=10)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    while arduino.inWaiting()==0:
        camera_on(cap,False)
    data = arduino.readline()
    return data


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markAttendance(name,frame):
    today = date.today()
    dateString = today.strftime("%d-%m-%Y")
    mList = os.listdir('Attendance')
    c = mList.count(dateString)
    if(c==0):
        os.mkdir(f'Attendance/{dateString}')
    tList = os.listdir(f'Attendance/{dateString}')
    cc = tList.count(f'Attendance_{dateString}.csv')
    if(cc==0):
        f =open(f'Attendance/{dateString}/Attendance_{dateString}.csv', 'w')
        f.writelines('NAME,TIME,DATE,TEMPERATURE\n')
    f=open(f'Attendance/{dateString}/Attendance_{dateString}.csv', 'r+')
    myDataList = f.readlines()
    nameList = []
    for line in myDataList:
        entry = line.split(',')
        nameList.append(entry[0])
    if name not in nameList:
        now = datetime.now()
        dtString = now.strftime('%H:%M:%S')
        value = write_read('t')
        f.writelines(f'{name},{dtString},{dateString},{value}\n')
        cv2.imwrite(filename=f'Attendance/{dateString}/{name}.jpg', img=frame)
        #cv2.imshow("Captured Image", cv2.imread(f'{name}.jpg'))
        print("Attendance done! for",dateString)
        print("Image saved! for",name)
        print("Your body temperature",value)

        
path = 'Training_images'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def camera_on(cap,flag):
    success, frame = cap.read()
    imgS = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            if flag:
                markAttendance(name,frame)
    cv2.imshow('Webcam', frame)
    cv2.waitKey(1)


encodeListKnown = findEncodings(images)
print('Encoding Complete')
cap = cv2.VideoCapture(0)
while True:
    camera_on(cap,True)
