import cv2
import numpy as np

medName = 'algopirin'
numberOfImage = 0

camera = cv2.VideoCapture(1)

while True:
    success, imgOrignal = camera.read()
    createdDataImage = np.asarray(imgOrignal)
    createdDataImage = cv2.resize(createdDataImage, (500, 500))
    cv2.imshow("Make Image", createdDataImage)
    cv2.rectangle(createdDataImage, (167, 221), (226, 300), (255, 0, 0), 3)

    key = cv2.waitKey(1)
    if key == ord("k"):
        cv2.rectangle(createdDataImage, (167, 221), (226, 300), (0, 255, 0), 3)
        croppedImage = createdDataImage[221:300, 167:226]
        cv2.imwrite("image" + str(numberOfImage) + ".jpg", croppedImage)
        cv2.putText(createdDataImage, 'Elkészült képek száma: ' + str(numberOfImage), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 4)

        numberOfImage += 1
    elif key == ord("q"):
        break