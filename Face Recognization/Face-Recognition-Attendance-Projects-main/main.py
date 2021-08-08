import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import serial

def write_read():
    arduino.write(bytes('t', 'utf-8'))
    while arduino.inWaiting()==0:
        camera_on(cap)
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
    today = datetime.today()
    dateString = today.strftime("%d-%m-%Y")
    now = datetime.now()
    dtString = now.strftime('%H:%M:%S')
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
        print("************************************************************************")
        print("Welcome",name)
        print("Your face has been Registered")
        print("Kindly register your body temperature for 5 seconds")
        value = write_read()
        f.writelines(f'{name},{dtString},{dateString},{value}\n')
        cv2.imwrite(filename=f'Attendance/{dateString}/{name}.jpg', img=frame)
        #cv2.imshow("Captured Image", cv2.imread(f'{name}.jpg'))
        print("Attendance done!")
        print("Image saved!")
        print("Your body temperature is",value)
        print("************************************************************************")


def camera_on(cap):
    name=" "
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
    return name,frame


arduino = serial.Serial(port='COM3', baudrate=9600, timeout=10)
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
encodeListKnown = findEncodings(images)
print('Encoding Complete')
cap = cv2.VideoCapture(0)
count=0
prev ="True"
while True:
    name,frame=camera_on(cap)
    if name==" ":
        count=0
        cv2.destroyAllWindows()
        continue
    cv2.imshow('Webcam', frame)
    cv2.waitKey(1)
    if prev == name :
        count+= 1
    else:
        prev=name
        count=0
    if count >=20:
        markAttendance(name,frame)
