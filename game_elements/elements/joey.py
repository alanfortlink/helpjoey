# the main character

from game_elements.base.element import *

class Joey(Element):
    def __init__(self, x, y):
        Element.__init__(self, ["../game_elements/resources/images/joey.png"], x, y, 50, 80)