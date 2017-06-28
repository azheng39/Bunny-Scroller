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
            start = False #Start the game
            gg = False #Collided, game reset

            ''' Font '''
            myfont = pygame.font.Font("../assets/title.ttf", 18)

            ''' Screen Text '''
            startText = myfont.render("S to Start", 0, (0,0,0))
            endText = myfont.render("GGWP", 0, (0,0,0))
            textYouDied = myfont.render("YOU DIED", 0, (0,0,0))
            textRestart = myfont.render("R to Restart", 0, (0,0,0))
            textQuit = myfont.render("Q to Quit", 0, (0,0,0))

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

                        ''' Bunny jump '''
                        if event.key == pygame.K_UP:
                            bun.jump()

                        ''' Reset game '''
                        if event.key == pygame.K_r:
                            bun.reinit()
                            obs.reinit()
                            score = 0
                            gg = False
                            start = False
                            obs.velocity = 10

                        ''' Quit game '''
                        if event.key == pygame.K_q:
                            done = True

                        ''' Start game '''
                        if event.key == pygame.K_s:
                            start = True

                ''' Draw background image '''
                screen.blit(backGround.image, (0,0))
                screen.blit(backGround.image, backGround.rect)

                ''' Collision '''
                if bun.rect.colliderect(obs.rect):
                    bun.collide()
                    gg = True

                ''' Game over '''
                if gg:
                    screen.blit(textYouDied, (500,500))
                    screen.blit(textRestart, (400,400))
                    bun.pauseBunny()
                    obs.pauseObstacle()

                    ''' Highscore I/O '''
                    if score > highscore:
                        highscore = score
                        scorefile = open("../assets/scores.txt", "w")
                        scorefile.write(str(highscore))
                        scorefile.close()

                ''' Game start '''
                if start:

                    ''' Score '''
                    label = myfont.render("Score: {0}".format(score), 0, (0, 0, 0))
                    texths = myfont.render("High Score: {0}".format(highscore), 0, (0,0,0))
                    screen.blit(label, (900, 10))
                    screen.blit(texths, (900, 40))
                    if not gg and start:
                        score += 1

                    ''' Draw objects '''
                    bun.draw(screen)
                    bunSprite.update()

                    obs.draw(screen)
                    obsSprite.update()

                    ''' Difficulty Levels '''
                    if bun.counter > 0:
                        obs.velocity = 10

                    if bun.counter > 400:
                        obs.velocity = 15

                    if bun.counter > 800:
                        obs.velocity = 20

                ''' Start Screen '''
                if not start:
                    screen.blit(startText, (200,200))
                    screen.blit(textQuit, (300,300))

                ''' Screen update '''
                pygame.display.update()
                pygame.display.flip()

def main():
    BunnyGame()
main()
