# spring for joey to jump

from game_elements.base.element import *


class Spring(Element):
    def __init__(self, x, y, force=50, angle=90):
        element_id = "Spring_" + str(Element.nextId)
        Element.nextId += 1
        Element.__init__(self, ["../game_elements/resources/images/door.png"], x, y, 50, 50, element_id)
        self.force = force
        self.angle = angle