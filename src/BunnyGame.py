import pygame
from bunny import Bunny
from BackGround import Background
from obstacle import Obstacle
import ImageProcess

class BunnyGame():

        def __init__(self):
            pygame.init()

            ''' Game States '''
            done = False #Quit the game
            start = False
            gg = False #Collided, game reset

            ''' Font '''
            myfont = pygame.font.SysFont("../assets/Halo3.ttf", 18)

            ''' Screen Text '''
            startText = myfont.render("S to Start", 0, (0,0,0))
            endText = myfont.render("GGWP", 0, (0,0,0))
            textYouDied = myfont.render("YOU DIED", 0, (0,0,0))

            ''' Screen elements '''
            pygame.display.init()
            screen = pygame.display.set_mode((1024, 576))
            pygame.display.set_caption('Leila the Bunny')

            ''' Background '''
            white = (255,255,0)
            background = pygame.Surface(screen.get_size())
            background = background.convert()
            background.fill(white)

            backGround = Background('../assets/background.jpeg')

            screen.blit(background, (0,0))
            pygame.display.flip()
            screen.blit(backGround.image, backGround.rect)

            ''' Score '''
            score = 0
            highscore = 0

            ''' Score I/O '''
            scorefile = open("../assets/scores.txt", "r")
            highscore = int(scorefile.read())
            scorefile.close()

            ''' Objects '''
            bun = Bunny()
            bunSprite = pygame.sprite.RenderPlain(bun)

            obs = Obstacle()
            obsSprite = pygame.sprite.RenderPlain(obs)

            obs2 = Obstacle()
            obs2Sprite = pygame.sprite.RenderPlain(obs2)

            obs3 = Obstacle()
            obs3Sprite = pygame.sprite.RenderPlain(obs3)

            clock = pygame.time.Clock()

            ''' Music '''
            #pygame.mixer.init(22050, -16, 2, 4096)
            #pygame.mixer.music.load("../assets/song.mp3")
            #pygame.mixer.music.set_volume(.5)
            #pygame.mixer.music.play(-1)

            ''' Game Loop '''
            while not done:
                clock.tick(60)
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        done = True

                    elif event.type == pygame.KEYDOWN:

                        '''Jump'''
                        if event.key == pygame.K_UP:
                            bun.jump()
                            print("bun.jump()")

                        '''Reset'''
                        if event.key == pygame.K_r:
                            print("=======Reset=======")
                            bun.reinit()
                            obs.reinit()
                            score = 0
                            gg = False
                            start = False

                        '''Quit'''
                        if event.key == pygame.K_q:
                            print("=======Quit=======")
                            done = True

                        '''Start'''
                        if event.key == pygame.K_s:
                            start = True
                            print("=======Start=======")

                screen.blit(backGround.image, (0,0))
                screen.blit(backGround.image, backGround.rect)

                ''' Collision '''
                if bun.rect.colliderect(obs.rect):
                    bun.collide()
                    gg = True

                ''' GGEZ '''
                if gg:
                    screen.blit(textYouDied, (500,500))
                    bun.pauseBunny()
                    obs.pauseObstacle()
                    if score > highscore:
                        highscore = score
                        scorefile = open("../assets/scores.txt", "w")
                        scorefile.write(str(highscore))
                        scorefile.close()

                if start:
                    ''' Score '''
                    label = myfont.render("Score: {0}".format(score), 0, (0, 0, 0))
                    texths = myfont.render("High Score: {0}".format(highscore), 0, (0,0,0))
                    screen.blit(label, (900, 10))
                    screen.blit(texths, (900, 40))
                    if not gg and start:
                        score += 1
                    ''' Draw objects once Start = True 0'''
                    bun.draw(screen)
                    bunSprite.update()

                    obs.draw(screen)
                    obsSprite.update()

                    ''' Difficulty Levels '''
                    #if bun.counter > 0:

                    #if bun.counter > 200:

                    #if bun.counter > 300:


                ''' Start Screen '''
                if not start:
                    screen.blit(startText, (200,200))

                pygame.display.update()
                pygame.display.flip()

def main():
    BunnyGame()
main()
