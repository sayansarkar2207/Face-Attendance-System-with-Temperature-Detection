import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import serial
import pyttsx3


def write_read():
    arduino.write(bytes('t', 'utf-8'))
    while arduino.inWaiting()==0:
        name,frame=camera_on(cap)
        cam_show(frame)
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
    dt=today.strftime("%m-%d-%Y")
    now = datetime.now()
    dtString = now.strftime('%H:%M:%S')
    mList = os.listdir('Attendance')
    c = mList.count(dateString)
    if(c==0):
        os.mkdir(f'Attendance/{dateString}')
    tList = os.listdir(f'Attendance/{dateString}')
    cc = tList.count(f'Attendance_{dateString}_IN.csv')
    cc1 = tList.count(f'Attendance_{dateString}_OUT.csv')
    if(cc==0):
        f =open(f'Attendance/{dateString}/Attendance_{dateString}_IN.csv', 'w')
        f.writelines('NAME,IN TIME,IN TEMPERATURE\n')
    if(cc1==0):
        f =open(f'Attendance/{dateString}/Attendance_{dateString}_OUT.csv', 'w')
        f.writelines('NAME,OUT TIME,OUT TEMPERATURE\n')
    f=open(f'Attendance/{dateString}/Attendance_{dateString}_IN.csv', 'r+')
    f1=open(f'Attendance/{dateString}/Attendance_{dateString}_OUT.csv', 'r+')
    myDataList = f.readlines()
    myDataList1 = f1.readlines()
    nameList = []
    nameList1 = []
    intime=[]
    for line in myDataList:
        entry = line.split(',')
        nameList.append(entry[0])
        intime.append(entry[1])
    for line1 in myDataList1:
        entry1 = line1.split(',')
        nameList1.append(entry1[0])
    if name not in nameList:
        print("************************************************************************")
        print("Welcome",name)
        engine.say("Welcome"+name)
        engine.runAndWait()
        print("Your face has been Registered")
        engine.say("Your face has been Registered")
        engine.runAndWait()
        print("Kindly register your body temperature for 5 seconds")
        engine.say("Kindly register your body temperature for 5 seconds")
        engine.runAndWait()
        value =float(write_read())
        if value>float(99.7):
            engine.say("Your body temperature is "+format(value,".1f")+" , please keep a check on your health")
            engine.runAndWait()
            engine.say("You are not eligible to mark your attendance as per Covid 19 protocol")
            engine.runAndWait()
            f.writelines(f'{name},Not Eligible,{format(value,".1f")}\n')
            cv2.imwrite(filename=f'Attendance/{dateString}/{name}_IN.jpg', img=frame)
        else:
            f.writelines(f'{name},{dtString},{format(value,".1f")}\n')
            cv2.imwrite(filename=f'Attendance/{dateString}/{name}_IN.jpg', img=frame)
            #cv2.imshow("Captured Image", cv2.imread(f'{name}.jpg'))
            print("Attendance done!")
            engine.say("Attendance done! on "+dt)
            engine.runAndWait()
            print("Your in time is",dtString)
            engine.say("Your in time is "+dtString)
            engine.runAndWait()
            print("Image saved!")
            engine.say("Image saved!")
            engine.runAndWait()
            print("Your body temperature is",format(value,".1f"),"*F")
            engine.say("Your body temperature is "+format(value,".1f")+" degree Fahrenheit")
            engine.runAndWait()
            engine.say("Thank you "+name+" for marking your attendance")
            engine.runAndWait()
            print("************************************************************************")
    elif name not in nameList1:
        if intime[nameList.index(name)]=="Not Eligible":
            engine.say(name+", Please go back to your home and isolate yourself")
            engine.runAndWait()
        else:
            time=(int(intime[nameList.index(name)][3:5])+2)%60
            time1=int(intime[nameList.index(name)][0:2])+int((int(intime[nameList.index(name)][3:5])+5)/60)
            if(int(dtString[0:2])>time1) or (int(dtString[0:2])==time1 and int(dtString[3:5])>time):
                print("************************************************************************")
                print("Good bye",name)
                engine.say("Good Bye"+name)
                engine.runAndWait()
                print("Your face has been Registered")
                engine.say("Your face has been Registered")
                engine.runAndWait()
                print("Kindly register your body temperature for 5 seconds")
                engine.say("Kindly register your body temperature for 5 seconds")
                engine.runAndWait()
                value =float(write_read())
                f1.writelines(f'{name},{dtString},{format(value,".1f")}\n')
                cv2.imwrite(filename=f'Attendance/{dateString}/{name}_OUT.jpg', img=frame)
                #cv2.imshow("Captured Image", cv2.imread(f'{name}.jpg'))
                print("Attendance done!")
                engine.say("Attendance done! on "+dt)
                engine.runAndWait()
                print("Your out time is",dtString)
                engine.say("Your out time is "+dtString)
                engine.runAndWait()
                print("Image saved!")
                engine.say("Image saved!")
                engine.runAndWait()
                print("Your body temperature is",format(value,".1f"),"*F")
                engine.say("Your body temperature is "+format(value,".1f")+" degree Fahrenheit")
                engine.runAndWait()
                if value>float(99.7):
                    engine.say(" Your body temperature is high, please keep a check on your health")
                    engine.runAndWait()
                    engine.say("Please go back to your home and isolate yourself")
                    engine.runAndWait()
                engine.say("Thank you "+name+" for marking your attendance, Bye bye")
                engine.runAndWait()
                print("************************************************************************")
            else:
                engine.say(name+", you In time has already been registered")
                engine.runAndWait()
    else:
        engine.say(name+", your attendance has already been registered")
        engine.runAndWait()


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


def cam_show(frame):
    cv2.imshow('Webcam', frame)
    cv2.waitKey(1)


if __name__ == '__main__':
    engine = pyttsx3.init()
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
        cam_show(frame)
        if prev == name :
            count+= 1
        else:
            prev=name
            count=0
        if count >=10:
            count=0
            markAttendance(name,frame)
