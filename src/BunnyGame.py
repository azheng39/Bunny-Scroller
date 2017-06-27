import pygame
import os
from bunny import Bunny
import background
import obstacle

class BunnyGame():

        def __init__(self):
            pygame.init()

            ''' Game States '''
            done = False
            start = False

            ''' Font '''
            myfont = pygame.font.SysFont("../assets/Halo3.ttf", 18)

            ''' Screen Text '''
            startText = myfont.render("S to Start", 0, (0,0,0))
            endText = myfont.render("GGWP", 0, (0,0,0))

            pygame.display.init()
            screen = pygame.display.set_mode((1024, 576))
            pygame.display.set_caption('Leila the Bunny')

            bun = Bunny()
            kangSprite = pygame.sprite.RenderPlain(kang)

            clock = pygame.time.Clock()

            while not done:
                clock.tick(60)
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        done = True

                    elif event.type == pygame.KEYDOWN:

                        '''Jump'''
                        if event.key == pygame.K_UP:
                            bun.jump()

                        '''Reset'''
                        #if event.key == pygame.K_r:

                        '''Quit'''
                        if event.key == pygame.K_q:
                            done = True

                        '''Start'''
                        if event.type == pygame.K_s:
                            start = True
                            kang.draw(screen)
                        


                if not start:
                    screen.blit(startText, (200,200))

def main():
    BunnyGame()
main()
