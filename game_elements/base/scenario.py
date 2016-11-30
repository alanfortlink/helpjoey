# game scenario

from element import *
from image import *

class Scenario:
    def __init__(self, image, width, height):
        self.image = image if isinstance(image, Image) else Image(image)
        self.width = width
        self.height = height
        self.elements = []
        self.window = None

        self.image.resize(width, height)

    def addElement(self, element):
        self.elements.append(element)

    def draw(self, window):

        self.image.draw(window, ((0, 0), (self.width, self.height)))

        for element in self.elements:
            element.draw(window)

    def update(self):
        #if there is a scenario update, do it here
        for element in self.elements:
            element.update()