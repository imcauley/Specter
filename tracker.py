import numpy as np
import cv2
from matplotlib import pyplot as plt

class Tracker:
    def find_eyes(self, eyes, frame, lower, upper):
        """
        @author Isaac McAuley
        @date April 3, 2018

        find_eyes()

        input:
            -eyes, a 2d matrix of a captured picture of the
                    users eyes
            -frame, the current frame for which the eyes are
                    to be found
            -lower, lower colour range
            -upper, upper colour range

        output:
            -a list of tuples, first is the point on the frame
                where a matches point is found, second is a
                cv2 match object
        """

        eyes_hsv = cv2.cvtColor(eyes, cv2.COLOR_BGR2HSV)
        frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        eyes_mask = cv2.inRange(eyes_hsv, lower, upper)
        frame_mask = cv2.inRange(frame_hsv, lower, upper)

        # Initiate SIFT detector
        orb = cv2.ORB_create()

        # find the keypoints and descriptors with SIFT
        kp1, des1 = orb.detectAndCompute(frame_mask,None)
        kp2, des2 = orb.detectAndCompute(eyes_mask,None)

        # create BFMatcher object
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        # Match descriptors.
        matches = bf.match(des1,des2)

        # Sort them in the order of their distance.
        matches = sorted(matches, key = lambda x:x.distance)

        zipped = zip(kp1,matches)
        return(list(zipped))
