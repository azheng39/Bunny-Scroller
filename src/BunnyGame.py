import pygame
from bunny import Bunny
from BackGround import Background
import obstacle
import ImageProcess

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

            ''' Background '''
            white = (255,255,0)
            background = pygame.Surface(screen.get_size())
            print("Screen.get_size()")
            background = background.convert()
            print("background.convert()")
            background.fill(white)
            print("background.fill()")


            backGround = Background('../assets/background.jpeg')
            print("Assign background.jpeg to backGround.")

            screen.blit(background, (0,0))
            print("screen.blit(background, (0,0))")
            pygame.display.flip()
            print("pygame.display.flip()")
            screen.blit(backGround.image, backGround.rect)
            print("screen.blit(backGround.image, backGround.rect)")

            ''' Objects '''
            bun = Bunny()
            bunSprite = pygame.sprite.RenderPlain(bun)



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
                            print("bun.jump()")

                        '''Reset'''
                        if event.key == pygame.K_r:
                            print("Restart")

                        '''Quit'''
                        if event.key == pygame.K_q:
                            print("Quit")
                            done = True

                        '''Start'''
                        if event.key == pygame.K_s:
                            print("S pressed.")
                            start = True
                            print("Start set to True.")

                screen.blit(backGround.image, (0,0))
                screen.blit(backGround.image, backGround.rect)

                if start:
                    bun.draw(screen)
                    bunSprite.update()


                if not start:
                    screen.blit(startText, (200,200))

                pygame.display.update()
                pygame.display.flip()

def main():
    BunnyGame()
main()
