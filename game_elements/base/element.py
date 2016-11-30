# abstract class for each view element
# the x and y for the element is the top left of it

from game_elements.base.image import *


class Element:
    nextId = 1

    def __init__(self, images, x, y, width, height, element_id=None):
        if not element_id:
            element_id = Element.nextId
            Element.nextId += 1

        self.element_id = element_id
        self.images = [image if isinstance(image, Image) else Image(image) for image in images]
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.spritePosition = 0

        for image in self.images:
            image.resize(self.width, self.height)

    def draw(self, window):
        self.images[self.spritePosition].draw(window, (self.x, self.y, self.width, self.height))

    def update(self):
        self.spritePosition = (self.spritePosition + 1) % len(self.images)

    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def jump(self):
        pass
