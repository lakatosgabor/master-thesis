import numpy as np
import cv2
import pickle
import serial
from pyfirmata import Arduino, SERVO
from time import sleep

frameWidth = 640
frameHeight = 480
brightness = 180
threshold = 0.2
font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, brightness)

pickle_in = open("model_trained.p", "rb")  ## rb = READ BYTE
model = pickle.load(pickle_in)

port = 'COM3'
pin = 3
board = Arduino(port)
board.digital[pin].mode = SERVO

#ser = serial.Serial('COM3', 9600)

def rotateServo(pin):
    board.digital[pin].write(0)
    sleep(0.5)

    board.digital[pin].write(90)
    sleep(0.5)

    board.digital[pin].write(180)
    sleep(0.5)

    board.digital[pin].write(90)
    sleep(0.5)

    board.digital[pin].write(0)
    sleep(0.5)

def led_on_off(ser, isOn):
    if isOn == True:
        ser.write(b'H')
    elif isOn == False:
        ser.write(b'L')

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
    if classNo == 35 or classNo == 13 or classNo == 34:
        return 'Algopirin'
    return 'Searching...'


while True:
    success, imgOrignal = cap.read()

    img = np.asarray(imgOrignal)
    img = cv2.resize(img, (32, 32))
    img = preprocessing(img)
    cv2.imshow("Processed Image", img)
    img = img.reshape(1, 32, 32, 1)


    imgOrignal = cv2.resize(imgOrignal, (600, 600))
    cv2.imshow("Video Image", imgOrignal)


    predictions = model.predict(img)

    predClass = model.predict_step(img)
    classIndex = np.argmax(predClass)
    probabilityValue = np.amax(predictions)


    if probabilityValue > threshold:
        if (str(getCalssName(classIndex)) == 'Algopirin'):
            print('---------------------------------------------------##########################--------------------------------------')
            print(str(getCalssName(classIndex)) + ' találat' + ' ' + str(classIndex))
            board.digital[pin].write(180)
            sleep(0.5)
            board.digital[pin].write(90)
            sleep(0.5)
            break


    key = cv2.waitKey(1)
    if key == ord("q"):
        #led_on_off(ser, False)
        board.digital[pin].write(90)
        sleep(0.5)
        break

    #led_on_off(ser, True)
