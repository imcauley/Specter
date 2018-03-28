import cv2
import numpy as np

class Calibrator:
    def calibrate(self):
        cap = cv2.VideoCapture(0)

        while(1):

            # Take each frame
            _, frame = cap.read()
            match = np.zeros((300,150,3), np.uint8)
            frame = cv2.flip(frame, 1 )


            # Convert BGR to HSV

            # Bitwise-AND mask and original image
            #res = cv2.bitwise_and(frame,frame, mask= mask)

            cv2.rectangle(frame,(450,200),(750,350),(255,0,0),3)

            cv2.imshow('frame',frame)
            #cv2.imshow('mask',mask)

            key_press = cv2.waitKey(1) & 0xFF
            if key_press == ord(' '):
                match = frame[200:350, 450:750]
                min_skin, max_skin = self.get_minmax(match)
                cv2.destroyAllWindows()
                cap.release()
                return(match, min_skin, max_skin)
                break

            elif key_press == ord('q'):
                cv2.destroyAllWindows()
                break

    def get_minmax(self, skin):
        max_skin = [0,0,0]
        min_skin = [255,255,255]

        for r in skin:
            for c in r:
                if((c > max_skin).all()):
                    max_skin = c
                if((c < min_skin).all()):
                    min_skin = c

        print(min_skin)
        print(max_skin)

        return min_skin, max_skin
