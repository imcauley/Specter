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
    if(len(match) > 0):
        print(match[0].pt[0])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
