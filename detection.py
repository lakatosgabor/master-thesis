import numpy as np
import cv2
import pickle
from pyfirmata import Arduino, SERVO
from time import sleep

frameWidth = 640
frameHeight = 480
brightness = 180
threshold = 0.8
font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, brightness)

pickle_in = open("model_trained.p", "rb")  ## rb = READ BYTE
model = pickle.load(pickle_in)

def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def equalize(img):
    return cv2.equalizeHist(img)

def preprocessing(img):
    img = grayscale(img)
    img = equalize(img)
    img = img / 255
    return img

def getCalssName(classNo):
    if classNo == 0:
        return 'Algopirin'
    return 'Searching...'


while True:
    success, imgOrignal = cap.read()

    img = np.asarray(imgOrignal)
    img = cv2.resize(img, (200, 200))
    img = preprocessing(img)
    cv2.imshow("Processed Image", img)
    img = img.reshape(1, 200, 200, 1)


    imgOrignal = cv2.resize(imgOrignal, (600, 600))
    cv2.imshow("Video Image", imgOrignal)


    predictions = model.predict(img)

    predClass = model.predict_step(img)
    classIndex = np.argmax(predClass)
    probabilityValue = np.amax(predictions)


    if probabilityValue > threshold:
        if (str(getCalssName(classIndex)) == 'Algopirin'):
            print(str(getCalssName(classIndex)) + ' találat' + ' Class: ' + str(classIndex) + ' probabilityValue: ' + str(probabilityValue))

    key = cv2.waitKey(1)
    if key == ord("q"):
        sleep(0.5)
        break
