import pygame
from bunny import Bunny
from BackGround import Background
from obstacle import Obstacle
from cloud import Cloud
import ImageProcess

class BunnyGame():

        def __init__(self):
            pygame.init()

            ''' Game States '''
            done = False #Quit the game
            start = False #Start the game
            gg = False #Collided, game reset

            ''' Font '''
            titleFont = pygame.font.Font("../assets/title.ttf", 50)
            mainFont = pygame.font.Font("../assets/main.ttf", 18)
            diedFont = pygame.font.Font("../assets/died.ttf", 60)

            ''' Screen Text '''
            titleText = titleFont.render("LEILA THE BUNNY", 0, (255,255,255))
            startText = mainFont.render("S to Start", 0, (0,0,0))
            endText = mainFont.render("GGWP", 0, (0,0,0))
            textYouDied = diedFont.render("YOU DIED", 0, (0,0,0))
            textRestart = mainFont.render("R to Restart", 0, (0,0,0))
            textQuit = mainFont.render("Q to Quit", 0, (0,0,0))

            ''' Screen elements '''
            pygame.display.init()
            screen = pygame.display.set_mode((1024, 576))
            pygame.display.set_caption('Leila the Bunny')

            ''' Background '''
            white = (255,255,255)
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

            cloud1 = Cloud()
            cloud1Sprite = pygame.sprite.RenderPlain(cloud1)

            clock = pygame.time.Clock()

            ''' Music '''
            pygame.mixer.init(22050,-16,2,4096)
            pygame.mixer.music.load("../assets/song.mp3")
            pygame.mixer.music.set_volume(.5)
            pygame.mixer.music.play(-1)
    
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
                            obs2.reinit()
                            obs3.reinit()
                            cloud1.reinit()
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
                
                if bun.rect.colliderect(obs2.rect):
                    bun.collide()
                    gg = True
                    
                if bun.rect.colliderect(obs3.rect):
                    bun.collide()
                    gg = True

                ''' Game over '''
                if gg:
                    screen.blit(textYouDied, (400,10))
                    screen.blit(textRestart, (460,80))
                    bun.pauseBunny()
                    obs.pauseObstacle()
                    obs2.pauseObstacle()
                    obs3.pauseObstacle()
                    cloud1.pauseCloud()

                    ''' Highscore I/O '''
                    if score > highscore:
                        highscore = score
                        scorefile = open("../assets/scores.txt", "w")
                        scorefile.write(str(highscore))
                        scorefile.close()

                ''' Game start '''
                if start:

                    ''' Score '''
                    label = mainFont.render("Score: {0}".format(score), 0, (0, 0, 0))
                    texths = mainFont.render("High Score: {0}".format(highscore), 0, (0,0,0))
                    screen.blit(label, (850, 10))
                    screen.blit(texths, (850, 40))
                    if not gg and start:
                        score += 1

                    ''' Draw objects '''
                    bun.draw(screen)
                    bunSprite.update()

                    obs.draw(screen)
                    obsSprite.update()
                
                    obs2.draw(screen)
                    obs2Sprite.update()
                    
                    obs3.draw(screen)
                    obs2Sprite.update()
                     
                    cloud1.draw(screen)
                    cloud1Sprite.update()

                    ''' Difficulty Levels '''
                    obs3.velocity = 0
                    for n in range(20):
                        if bun.counter >= 200 * n:
                            obs.velocity = 10 + 0.5 * n
                            obs2.velocity = 10 + 0.5 * n
                    
                    if bun.counter >1000:
                        bun.lvlspeed = 4
                        
                    if bun.counter >= 2000:
                        obs3.velocity = 7
                        bun.lvlspeed = 3
                if not start:
                    screen.blit(titleText, (300,20))
                    screen.blit(startText, (460,85))
                    screen.blit(textQuit, (455,105))

                ''' Screen update '''
                pygame.display.update()
                pygame.display.flip()

def main():
    BunnyGame()
main()
