# abstract class for each view element
# the x and y for the element is the top left of it

from game_elements.base.image import *
from math import sqrt
from math import sin
from math import cos
from math import radians


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
        self.time = 0
        self.px = 0
        self.py = 0
        self.vox = 0
        self.voy = 0
        self.jumping = False

        for image in self.images:
            image.resize(self.width, self.height)

    def draw(self, window):
        self.images[self.spritePosition].draw(window, (self.x-self.px, self.y-self.py, self.width, self.height))

    def update(self):
        self.spritePosition = (self.spritePosition + 1) % len(self.images)
        if self.jumping:
            self.time += 1.0/3.0

            self.px = self.vox * self.time
            self.py = self.voy * self.time + ((-10 * pow(self.time, 2)) / 2)

            # print self.vox, self.time, self.px, self.py

            if self.px < 0 or self.py < 0:
                self.jumping = False
                self.time, self.px, self.py = 0, 0, 0

    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def isColliding(self, e):
        dist = sqrt( (pow(e.y - self.y, 2)) + (pow(e.x - self.x, 2)) )
        return (dist <= self.width/2 + e.width/2) or (dist <= self.height/2 + e.height/2)

    def jump(self, force, angle):
        if not self.jumping:
            self.jumping = True
            self.time = 0
            self.vox = force * cos(radians(angle))
            self.voy = force * sin(radians(angle))

            # print force, angle, cos(radians(angle)), sin(radians(angle)), self.vox, self.voy

            self.px = 0
            self.py = 0