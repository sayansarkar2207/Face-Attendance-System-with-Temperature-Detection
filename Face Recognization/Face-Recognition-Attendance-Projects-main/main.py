import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import serial
import pyttsx3
import speech_recognition as sr
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import argparse

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
    engine = pyttsx3.init()
    category="Employee"
    if(name=="Visitor"):
        category=name
        engine.say("Please say your name")
        engine.runAndWait()
        text=rec_audio()
        engine.say("Please confirm that "+text+" is your name or not")
        engine.runAndWait()
        text1=rec_audio()
        if(text1=="yes"):
            name=text
        else:
            engine.say("Please register your face again")
            engine.runAndWait()
            return
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
        f.writelines('NAME,IN TIME,IN TEMPERATURE,CATEGORY\n')
    if(cc1==0):
        f =open(f'Attendance/{dateString}/Attendance_{dateString}_OUT.csv', 'w')
        f.writelines('NAME,OUT TIME,OUT TEMPERATURE,CATEGORY\n')
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
            f.writelines(f'{name},Not Eligible,{format(value,".1f")},{category}\n')
            cv2.imwrite(filename=f'Attendance/{dateString}/{name}_IN.jpg', img=frame)
        else:
            print("Your body temperature is",format(value,".1f"),"*F")
            engine.say("Your body temperature is "+format(value,".1f")+" degree Fahrenheit")
            engine.runAndWait()
            engine.say("To mark your attendance please put on your mask")
            engine.runAndWait()
            #cv2.destroyAllWindows()
            if(mask_detect()):
                f.writelines(f'{name},{dtString},{format(value,".1f")},{category}\n')
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
                engine.say("Thank you "+name+" for marking your attendance")
                engine.runAndWait()
                print("************************************************************************")
            else:
                engine.say("As you did not wore your mask, your attendance could not be registered")
                engine.say("Please register your face again")
                engine.runAndWait()
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
                print("Your body temperature is",format(value,".1f"),"*F")
                engine.say("Your body temperature is "+format(value,".1f")+" degree Fahrenheit")
                engine.runAndWait()
                engine.say("To mark your attendance please put on your mask")
                engine.runAndWait()
                #cv2.destroyAllWindows()
                if(mask_detect()):
                    f1.writelines(f'{name},{dtString},{format(value,".1f")},{category}\n')
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
                    if value>float(99.7):
                        engine.say(" Your body temperature is high, please keep a check on your health")
                        engine.runAndWait()
                        engine.say("Please go back to your home and isolate yourself")
                        engine.runAndWait()
                    engine.say("Thank you "+name+" for marking your attendance, Bye bye")
                    engine.runAndWait()
                    print("************************************************************************")
                else:
                    engine.say("As you did not wore your mask, your attendance could not be registered")
                    engine.say("Please register your face again")
                    engine.runAndWait()
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
            cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255), 2)
        else:
            name="Visitor"
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255), 2)
    return(name,frame)

def cam_show(frame):
    cv2.imshow('Webcam', frame)
    cv2.waitKey(1)


def mask_detect():
    label1=" "
    print("[INFO] starting video stream...")
    tcount=0
    mcount=0
    while mcount<50:
        if(tcount>100):
            break
        success, frame1 = cap.read()
        frame2=cv2.resize(frame1, (0, 0), None, 0.25, 0.25)
        (locs, preds) = detect_and_predict_mask(frame2, faceNet, maskNet)
        for (box, pred) in zip(locs, preds):
            (mask, withoutMask) = pred
            label = "Mask" if mask > withoutMask else "No Mask"
            label1=label
            color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
            label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)
            (x1,y1,x2,y2)=box
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(frame1, (x1, y1), (x2, y2), color, 2)
            cv2.rectangle(frame1, (x1, y2 - 35), (x2, y2), color, cv2.FILLED)
            cv2.putText(frame1, label, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255), 2)
        if(label1=='Mask'):
            mcount+=1
            tcount=0
        else:
            tcount+=1
            mcount=0
        cv2.imshow("Webcam", frame1)
        cv2.waitKey(1)
    if(mcount>49):
        return True
    else:
        return False


def rec_audio():
    text=" "
    with sr.Microphone(device_index =0, sample_rate = 48000,chunk_size = 2048) as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        print("Say Something")
        audio = r.listen(source,timeout=10,phrase_time_limit=7)
        try:
            text = r.recognize_google(audio,language='en-in')
            print("you said: " + text)
        except sr.UnknownValueError:
            print("I cannot understand what you said")
        except sr.RequestError as e:
            print("I cannot connect to the service; {0}".format(e))
    return text



def detect_and_predict_mask(frame, faceNet, maskNet):
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300),(104.0, 177.0, 123.0))
    faceNet.setInput(blob)
    detections = faceNet.forward()
    faces = []
    locs = []
    preds = []
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > args["confidence"]:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            (startX, startY) = (max(0, startX), max(0, startY))
            (endX, endY) = (min(w - 1, endX), min(+h - 1, endY))
            face = frame[startY:endY, startX:endX]
            face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
            face = cv2.resize(face, (224, 224))
            face = img_to_array(face)
            face = preprocess_input(face)
            faces.append(face)
            locs.append((startX, startY, endX, endY))
    if len(faces) > 0:
        faces = np.array(faces, dtype="float32")
        preds = maskNet.predict(faces, batch_size=32)
    return (locs, preds)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--face", type=str,default="face_detector",help="path to face detector model directory")
    ap.add_argument("-m", "--model", type=str,default="mask_detector.model",help="path to trained face mask detector model")
    ap.add_argument("-c", "--confidence", type=float, default=0.5,help="minimum probability to filter weak detections")
    args = vars(ap.parse_args())
    print("[INFO] loading face detector model...")
    prototxtPath = os.path.sep.join([args["face"], "deploy.prototxt"])
    weightsPath = os.path.sep.join([args["face"],"res10_300x300_ssd_iter_140000.caffemodel"])
    faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)
    print("[INFO] loading face mask detector model...")
    maskNet = load_model(args["model"])
    engine = pyttsx3.init()
    engine.say("Starting")
    engine.runAndWait()
    r = sr.Recognizer()
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
    print("\t*********************************************************")
    print("\t***** Welcome To Face Recognition Attendance System *****")
    print("\t*********************************************************")
    engine.say("Welcome To Face Recognition Attendance System")
    engine.runAndWait()
    engine.say("If you want to start the recognization please say start")
    engine.runAndWait()
    #cap = cv2.VideoCapture(0)
    count=0
    fcount=500
    prev ="True"
    cap = cv2.VideoCapture(0)
    while True:
        if(count==0 and fcount==500):
            cap.release()
            cv2.destroyAllWindows()
            text=rec_audio()
            if(text=="stop"):
                engine.say("Thank you for using Face Recognization attendance system")
                engine.runAndWait()
                break
            if(text!="start"):
                continue
            fcount=0
            count=1
            cap = cv2.VideoCapture(0)
        name,frame=camera_on(cap)
        if name==" ":
            count=0
            fcount+=1
            if(fcount==500):
                engine.say("Shutting down camera, going on power saving mode")
                engine.runAndWait()
            cam_show(frame)
            continue
        cam_show(frame)
        if prev == name :
            count+= 1
        else:
            prev=name
            count=1
        if count >=15:
            count=0
            fcount=0
            markAttendance(name,frame)
