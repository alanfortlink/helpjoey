from game_elements.base.scenario import *
from game_elements.elements.door import *
from game_elements.elements.joey import *
from game_elements.elements.floor import *
from game_elements.elements.spring import *
import random
import pygame

window_size = (1000, 480)
fps = 60
move_speed = 100

scenario = Scenario("../game_elements/resources/images/scenario1.jpg", *window_size)
scenario.addElement(Door(0, 350))
scenario.addElement(Spring(100, 350))
floor = Floor([(i, 400) for i in range(window_size[0])], [])
scenario.addElement(floor)
joey = Joey(0, 400)
scenario.addElement(joey)

window = pygame.display.set_mode(window_size)

running = True

clock = pygame.time.Clock()
count = 0

while running:
    count += clock.tick()

    if count > 1000.0/fps:
        count = 0
        scenario.update(move_speed, fps)

    scenario.draw(window)

    pygame.display.flip()

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False