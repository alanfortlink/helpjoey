# door of joey's house

from game_elements.base.element import *

class Door(Element):
    def __init__(self, x, y):
        Element.__init__(self, ["../game_elements/resources/images/door.png"], x, y, 50, 50)