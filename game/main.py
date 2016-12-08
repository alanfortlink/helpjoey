from opencv.provider import *
from opencv.recognizer import *

# tracking step

provider = Provider()
recog = Recognizer()

game_frame = None
last = (0, 0)

while True:
    ret, frame = provider.get_image()

    cv2.imshow("Tracking", frame)
    last = recog.track(game_frame, frame, last)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

provider.close()


# recognizing step

recog.get_objects(game_frame)

# playing step


from game_elements.base.scenario import *
from game_elements.elements.door import *
from game_elements.elements.joey import *
from game_elements.elements.floor import *
from game_elements.elements.spring import *
import pygame

window_size = (1000, 480)
fps = 60
move_speed = 100

scenario = Scenario("../game_elements/resources/images/scenario1.jpg", *window_size)
scenario.add_element(Door(0, 350))



floor = Floor([(i, 400) for i in range(window_size[0])], [])
scenario.add_element(floor)
joey = Joey(0, 400)
scenario.add_element(joey)

window = pygame.display.set_mode(window_size)

running = True

clock = pygame.time.Clock()
count = 0

while running:
    fps = clock.get_fps()
    fps = fps if fps != 0 else 30
    count += clock.tick()

    if count > 1000.0/fps:
        count = 0
        scenario.update(move_speed, fps)

    scenario.draw(window)

    pygame.display.flip()

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
