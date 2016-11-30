# sprite image
import pygame
import os

class Image:
    def __init__(self, path):
        if not path:
            self.image = None
        else:
            self.image = pygame.image.load(os.getcwd()+"/"+path)

    def draw(self, window, rect):
        if self.image:
            window.blit(self.image, rect)

    def resize(self, width, height):
        if self.image:
            self.image = pygame.transform.scale(self.image, (width, height))