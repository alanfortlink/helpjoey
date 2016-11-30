from game_elements.base.scenario import *
from game_elements.elements.door import *
from game_elements.elements.joey import *
from game_elements.elements.floor import *
import random
import pygame

window_size = (640, 480)
fps = 30
move_speed = 100

scenario = Scenario("../game_elements/resources/images/scenario1.png", *window_size)
scenario.addElement(Door(0, 0))
floor = Floor([(i, 200) for i in range(640)], [])
scenario.addElement(floor)
joey = Joey(0, 400)

window = pygame.display.set_mode(window_size)

running = True

clock = pygame.time.Clock()
count = 0

while running:
    count += clock.tick()

    if count > 1000/fps:
        count = 0
        scenario.update()
        joey.move(move_speed/fps, 0)

        try:
            joey.setPosition(joey.x, [pos for pos in floor.points if int(pos[0]) == int(joey.x)][0][1])
        except:
            #end of the game
            pass

    scenario.draw(window)
    joey.draw(window)

    pygame.display.flip()

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False