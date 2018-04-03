import cv2
import numpy as np
import time
import csv
from calibrator import Calibrator
from tracker import Tracker
from graph import Graph


cal = Calibrator()
eyes, lower, upper = cal.calibrate()


cap = cv2.VideoCapture(0)
prev_x = 0
prev_y = 0

data = []

while(True):
    ret, frame = cap.read()

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    track = Tracker()
    match = track.find_eyes(eyes, frame, lower, upper)


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

    if((avg_x - prev_x) < 100):
        avg_x = int((avg_x + prev_x) / 2)

    if((avg_y - prev_y) < 100):
        avg_y = int((avg_y + prev_y) / 2)


    cv2.circle(rgb,(avg_x,avg_y), 5, (0,0,255), 1)
    frame = cv2.flip(frame, 1 )
    cv2.imshow('frame', rgb)

    prev_x = avg_x
    prev_y = avg_y

    data.append([avg_x, avg_y])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



timestr = time.strftime("%Y%m%d-%H%M%S")

with open((timestr + '.csv'), 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)

cap.release()
cv2.destroyAllWindows()

if input("Generate graphs? y/n: ") == 'y':
    graph = Graph(timestr)
    graph.input_data = graph.parse_data()
    graph.generate_graph()
