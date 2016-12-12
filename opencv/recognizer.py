from provider import *
import cv2


class Recognizer:
    def __init__(self):
        pass

    def get_objects(self, source):
        return []

    def track(self, source, frame, last=(0, 0)):
        return last

    @staticmethod
    def get_contours(frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.bilateralFilter(gray, 11, 17, 17)
        edged = cv2.Canny(gray, 30, 200)
        ret, thresh = cv2.threshold(edged, 127, 255, cv2.THRESH_BINARY)
        return cv2.findContours(thresh, 1, 2)

    @staticmethod
    def findBounds(frame):
        contours, hierarchy = Recognizer.get_contours(frame)
        max_area = 0.0
        for contour in contours:
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
            area = cv2.contourArea(contour)
            # if our approximated contour has four points, then
            # we can assume that we have found our screen
            if len(approx) == 4 and area > max_area:
                screenCnt = approx
                max_area = area

        # print screenCnt
        # cv2.drawContours(frame, [screenCnt], -1, (0, 255, 0), 3)
        (H, mask) = cv2.findHomography(screenCnt.astype('single'),
                                       np.array([[[0., 0.]], [[800., 0.]], [[800., 600.]], [[0., 600.]]],
                                                dtype=np.single))
        final_image = cv2.warpPerspective(frame, H, (800, 600))
        # cv2.imshow("Bound", final_image)
        # cv2.waitKey(0)
        # return screenCnt

        return final_image