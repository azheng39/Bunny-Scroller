import pygame

class BunnyGame():

        def __init__(self):
            pygame.init()
            done = False
            screen = pygame.display.set_model((500, 500))
            pygame.display.set_caption('Leila the Bunny')

            backGround = Background.Background('../assets/background.png')

            while not done:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                done = True
                    pygame.display.flip()
