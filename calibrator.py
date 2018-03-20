import cv2
import numpy as np

class Calibrator:
    def calibrate():
        cap = cv2.VideoCapture(0)

        while(1):

            # Take each frame
            _, frame = cap.read()
            match = np.zeros((300,150,3), np.uint8)
            frame = cv2.flip(frame, 1 )


            # Convert BGR to HSV
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # define range of blue color in HSV
            lower_blue = np.array([50,100,50])
            upper_blue = np.array([200,255,180])

            # Threshold the HSV image to get only blue colors
            mask = cv2.inRange(hsv, lower_blue, upper_blue)
            # Bitwise-AND mask and original image
            res = cv2.bitwise_and(frame,frame, mask= mask)

            cv2.rectangle(frame,(450,200),(750,350),(255,0,0),3)

            cv2.imshow('frame',frame)
            #cv2.imshow('mask',mask)

            key_press = cv2.waitKey(1) & 0xFF
            if key_press == ord(' '):
                match = frame[200:350, 450:750]
                cv2.destroyAllWindows()
                return(match)
                break

            elif key_press == ord('q'):
                cv2.destroyAllWindows()
                break
