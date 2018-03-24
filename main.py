import cv2
import numpy as np
from calibrator import Calibrator
from tracker import Tracker
from matplotlib import pyplot as plt


lower = np.array([50,100,50])
upper = np.array([200,255,180])

cal = Calibrator()
eyes = cal.calibrate(lower, upper)

#cv2.imwrite('eyes.jpg', eyes)

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    track = Tracker()
    match = track.find_eyes(eyes, frame)


    total_x = 0
    total_y = 0

    avg_x = 0
    avg_y = 0

    if(len(match) > 0):
        for m in match:
            #if(m[1].distance > 40):
            total_x = total_x + m[0].pt[0]
            total_y = total_y + m[0].pt[1]

        avg_x = total_x / len(match)
        avg_y = total_y / len(match)

    avg_x = int(avg_x)
    avg_y = int(avg_y)


    cv2.circle(rgb,(avg_x,avg_y), 5, (0,0,255), 1)
    cv2.imshow('frame', rgb)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
