import numpy as np
import cv2
from matplotlib import pyplot as plt


class Tracker:
    def find_eyes(self, eyes, frame):
        # Initiate SIFT detector
        orb = cv2.ORB_create()

        # find the keypoints and descriptors with SIFT
        kp1, des1 = orb.detectAndCompute(frame,None)
        kp2, des2 = orb.detectAndCompute(eyes,None)

        # create BFMatcher object
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        # Match descriptors.
        matches = bf.match(des1,des2)

        # Sort them in the order of their distance.
        matches = sorted(matches, key = lambda x:x.distance)

        return(kp1)
