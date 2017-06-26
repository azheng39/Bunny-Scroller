import pygame
import os

class BunnyGame():

        def __init__(self):
            pygame.init()

            ''' Game States '''
            done = False
            start = False

            ''' Font '''
            font = pygame.font.SysFont("../assets/Halo3.ttf", 18)

            ''' Screen Text '''
            startText = font.render("S to Start", 0, (0,0,0))
            endText = font.render("GGWP", 0, (0,0,0))

            pygame.display.init()
            screen = pygame.display.set_mode((1024, 576))
            pygame.display.set_caption('Leila the Bunny')

            clock = pygame.time.Clock()

            while not done:
                clock.tick(60)
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        done = True

                    elif event.type == pygame.KEYDOWN:

                        '''Jump'''
                        #if event.key == pygame.K_UP:
                        #    bunny.jump()

                        '''Quit'''
                        if event.key == pygame.K_q:
                            done = True

                        '''Start'''
                        if event.type == pygame.K_s:
                            start = True
                if not start:
                    screen.blit(startText, (200,200))

                pygame.display.flip()

def main():
    BunnyGame()
main()
