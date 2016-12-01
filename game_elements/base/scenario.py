# game scenario

from element import *
from image import *
from game_elements.elements.joey import *
from game_elements.elements.floor import *
from game_elements.elements.spring import *

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

    def update(self, move_speed, fps):
        #if there is a scenario update, do it here
        for element in self.elements:
            element.update()

            if isinstance(element, Joey):
                element.move(move_speed / fps, 0)

                floors = [x for x in self.elements if isinstance(x, Floor)]
                if len(floors) > 0:
                    floor = floors[0]
                    try:
                        element.setPosition(element.x,[pos for pos in floor.points if int(pos[0]) == int(element.x)][0][1] - element.height)
                    except:
                        #end of game
                        pass

                elementsColliding = [e for e in [x for x in self.elements if x != element] if element.isColliding(e)]
                if len(elementsColliding) > 0:
                    if len([x for x in elementsColliding if isinstance(x, Spring)]) > 0:
                        element.jump(50, 90)

                # for elColl in elementsColliding:
