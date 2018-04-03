import cv2
import numpy as np

class Calibrator:
    def calibrate(self):
        """
        @author Isaac McAuley
        @date April 3, 2018

        calibrate()

        input:
            -none

        output:
            -a 2d rgb image of the subsection of the frame

        """
        cap = cv2.VideoCapture(0)

        while(1):

            # Take each frame
            _, frame = cap.read()
            # Create empty object
            match = np.zeros((300,150,3), np.uint8)
            # Flip the image horizontally so the output looks normal
            frame = cv2.flip(frame, 1 )


            #Draw rectangle on frame
            show_frame = frame
            cv2.rectangle(show_frame,(450,200),(750,350),(255,0,0),3)

            #Show fram on screen
            cv2.imshow('frame',show_frame)

            #Get key press
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
        """
        @author Isaac McAuley
        @date April 3, 2018

        get_minmax()

        input:
            -2d image

        output:
            -tuple, first is the min shade in the frame, second
                    is the max shade of the frame
        """
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
