import pygame
import os
from bunny import Bunny
from BackGround import Background
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

            ''' Screen elements '''
            pygame.display.init()
            screen = pygame.display.set_mode((1024, 576))
            pygame.display.set_caption('Leila the Bunny')\


            white = (255,255,255)

            ''' Background '''
            background = pygame.Surface(screen.get_size())
            background = background.convert()
            background.fill(white) 


            backGround = Background('../assets/background.png')

            screen.blit(background, (0,0))
            pygame.display.flip()
            screen.blit(backGround.backgroundImage, backGround.rect)
           
            ''' Objects '''
            bun = Bunny()
            #bunSprite = pygame.sprite.RenderPlain(bun)

            clock = pygame.time.Clock()

            while not done:
                clock.tick(60)
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        done = True

                    elif event.type == pygame.KEYDOWN:

                        '''Jump'''
                        if event.key == pygame.K_UP:
                            print("UP")
                            bun.jump()

                        '''Reset'''
                        if event.key == pygame.K_r:
                            print("Restart")

                        '''Quit'''
                        if event.key == pygame.K_q:
                            print("Quit")
                            done = True

                        '''Start'''
                        if event.key == pygame.K_s:
                            print("Start")
                            start = True
                            bun.draw(screen)
                           # bunSprite.update()
                screen.blit(backGround.backgroundImage, (0,0))
                screen.blit(backGround.backgroundImage, backGround.rect)
                        


                if not start:
                    screen.blit(startText, (200,200))

def main():
    BunnyGame()
main()
