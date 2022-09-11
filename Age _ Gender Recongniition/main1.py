import cv2
import time
from playsound import playsound
import pygame
from numpy import swapaxes


def faceBox(faceNet, frame):
    frameHeight = frame.shape[0]
    frameWidth = frame.shape[1]
    blob=cv2.dnn.blobFromImage(frame, 1.0, (227, 227), [104, 117, 123], swapRB = False)
    faceNet.setInput(blob)
    detection = faceNet.forward()
    bbox =[]
    for i in range(detection.shape[2]):
        confidence = detection[0, 0, i, 2]
        if confidence> 0.7:
            x1 = int(detection[0, 0, i, 3]*frameWidth)
            y1 = int(detection[0, 0, i, 4]*frameHeight)
            x2 = int(detection[0, 0, i, 5]*frameWidth)
            y2 = int(detection[0, 0, i, 6]*frameHeight)
            bbox.append([x1, y1, x2, y2])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
    return frame, bbox


faceProto = "opencv_face_detector.pbtxt"
faceModel = "opencv_face_detector_uint8.pb"   

ageProto = "age_deploy.prototxt"
ageModel = "age_net.caffemodel"

genderProto = "gender_deploy.prototxt"
genderModel = "gender_net.caffemodel"

faceNet = cv2.dnn.readNet(faceModel, faceProto)
ageNet = cv2.dnn.readNet(ageModel, ageProto)
genderNet = cv2.dnn.readNet(genderModel, genderProto) 


MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(20-25)', '(25-35)', '(35-45)', '(45-55)', '(60-70)']
genderList = ['Male', 'Female']

video = cv2.VideoCapture(0)
padding = 20
start = time.time()
ageFound = -1
genderFound = "null"
while True:
    ret, frame = video.read()
    frame, bboxs = faceBox(faceNet, frame)
    for bbox in bboxs:
        face = frame[max(0,bbox[1]-padding):min(bbox[3]+padding,frame.shape[0]-1),max(0,bbox[0]-padding):min(bbox[2]+padding, frame.shape[1]-1)]
        blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB = False)
        genderNet.setInput(blob)
        genderPred = genderNet.forward()
        gender = genderList[genderPred[0].argmax()]

        ageNet.setInput(blob)
        agePred = ageNet.forward()
        age = ageList[agePred[0].argmax()]

        label = "{}, {}".format(gender, age)
        cv2.putText(frame, label, (bbox[0], bbox[1]- 10), cv2.FONT_HERSHEY_PLAIN, 0.8, (255, 255, 255), 2)
        #print(type(age))
        ageFound = age
        genderFound = gender
        #if(age == "(20-25)"): print("You are young")

    cv2.imshow("Age-Gender", frame)
    k = cv2.waitKey(1)
    end = time.time()
    #print(end- start)
    if k == ord('q') or int(end- start) == 3:
        break
if ageFound == "(20-25)" and gender == "Male":
    print(f"Your Age is: ", ageFound)
    print(f"Gender: ", gender)
    file = open('hipHop', 'r')
    lines = file.readlines()
    print('Music You May Like: \n ')
    for i in lines:
        print(i)
    pygame.mixer.init()
    pygame.mixer.music.load('Closer.mp3')
    pygame.mixer.music.play()
    video.release()
    cv2.destroyAllWindows()
    time.sleep(60)
    


if ageFound == "(20-25)" and gender == "Female":
    file = open('dance', 'r')
    lines = file.readlines()
    print('Music You May Like: ')
    for i in lines:
        print(i)

if ageFound == "(25-35)" and gender == "Male":
    file = open('jazz', 'r')
    lines = file.readlines()
    print('Music You May Like: ')
    for i in lines:
        print(i)
        break


if ageFound == "(25-35)" and gender == "Female":
    file = open('acoustic', 'r')
    lines = file.readlines()
    print('Music You May Like: ')
    for i in lines:
        print(i)

if ageFound == "(35-45)" and gender == "Male":
    file = open('classical', 'r')
    lines = file.readlines()
    print('Music You May Like: ')
    for i in lines:
        print(i)
        break


if ageFound == "(35-45)" and gender == "Female":
    file = open('classical', 'r')
    lines = file.readlines()
    print('Music You May Like: ')
    for i in lines:
        print(i)

if ageFound == "(45-55)" and gender == "Male":
    file = open('classical', 'r')
    lines = file.readlines()
    print('Music You May Like: ')
    for i in lines:
        print(i)
        break

if ageFound == "(45-55)" and gender == "Female":
    file = open('classical', 'r')
    lines = file.readlines()
    print('Music You May Like: ')
    for i in lines:
        print(i)

if ageFound == "(60-70)" and gender == "Male":
    file = open('classical', 'r')
    lines = file.readlines()
    print('Music You May Like: ')
    for i in lines:
        print(i)
        break

if ageFound == "(60-70)" and gender == "Female":
    file = open('classical', 'r')
    lines = file.readlines()
    print('Music You May Like: ')
    for i in lines:
        print(i)

video.release()
cv2.destroyAllWindows()