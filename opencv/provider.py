import numpy as np
import cv2


class Provider:
    def __init__(self):
        # self.cap = cv2.VideoCapture("http://10.42.0.185:8080/video?dummy=param.mjpg")
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.cv.CV_CAP_PROP_FPS, 1)

    def get_scenario(self):
        pass

    def get_image(self):
        ret, frame = self.cap.read()
        return ret, cv2.flip(frame, 1)

    def close(self):
        self.cap.release()
