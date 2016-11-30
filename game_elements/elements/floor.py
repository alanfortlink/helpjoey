# floor

from game_elements.base.element import *
import pygame


class Floor(Element):
    def __init__(self, points, angles):
        Element.__init__(self, [Image(None)], 0, 0, 0, 0)
        self.points = points
        self.angles = angles

    def draw(self, window):
        pygame.draw.lines(window, (0, 0, 0), False, self.points, 5)
