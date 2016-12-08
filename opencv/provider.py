import numpy as np
import cv2


class Provider:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def get_scenario(self):
        pass

    def get_image(self):
        ret, frame = self.cap.read()
        return ret, cv2.flip(frame, 1)

    def close(self):
        self.cap.release()
