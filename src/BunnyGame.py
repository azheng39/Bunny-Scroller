import pygame
from bunny import Bunny
from BackGround import Background
from obstacle import Obstacle
from cloud import Cloud
from platform import Platform
import ImageProcess

class BunnyGame():

        def __init__(self):
            pygame.init()

            ''' Game States '''
            done = False #Quit the game
            start = False #Start the game
            gg = False #Collided, game reset

            ''' Font '''
            titleFont = pygame.font.Font("../assets/title.ttf", 90)
            mainFont = pygame.font.Font("../assets/main.ttf", 18)
            diedFont = pygame.font.Font("../assets/died.ttf", 60)

            ''' Screen Text '''
            titleText = titleFont.render("LEILA THE BUNNY", 0, (255,255,255))
            startText = mainFont.render("S to Start", 0, (0,0,0))
            endText = mainFont.render("GGWP", 0, (0,0,0))
            youDiedText = diedFont.render("YOU DIED", 0, (200,27,27))
            restartText = mainFont.render("R to Restart", 0, (0,0,0))
            quitText = mainFont.render("Q to Quit", 0, (0,0,0))
            pauseText = mainFont.render("M to Mute", 0, (0,0,0))

            ''' Screen elements '''
            pygame.display.init()
            screen = pygame.display.set_mode((1024, 576))
            pygame.display.set_caption('Leila the Bunny')
            icon = pygame.image.load("../assets/icon.png")
            pygame.display.set_icon(icon)

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

            obs1 = Obstacle()
            obs1Sprite = pygame.sprite.RenderPlain(obs1)
        
            obs2 = Obstacle()
            obs2Sprite = pygame.sprite.RenderPlain(obs2)

            obs3 = Obstacle()
            obs3Sprite = pygame.sprite.RenderPlain(obs3)

            stage = Platform()
            stageSprite = pygame.sprite.RenderPlain(stage)

            cloud1 = Cloud(0)
            cloud1Sprite = pygame.sprite.RenderPlain(cloud1)

            cloud2 = Cloud(1)
            cloud2Sprite = pygame.sprite.RenderPlain(cloud2)

            clock = pygame.time.Clock()

            ''' Music '''
            paused = -1
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
                            obs1.reinit()
                            obs2.reinit()
                            obs3.reinit()
                            stage.reinit()
                            cloud1.reinit()
                            cloud2.reinit()
                            bun.jumpup = False
                            score = 0
                            gg = False
                            start = False
                            obs1.velocity = 10

                        ''' Quit game '''
                        if event.key == pygame.K_q:
                            done = True

                        ''' Start game '''
                        if event.key == pygame.K_s:
                            start = True

                        '''Pause/Unpause Music'''
                        if event.key == pygame.K_m:
                            paused = -paused

                ''' Draw background image '''
                screen.blit(backGround.image, (0,0))
                screen.blit(backGround.image, backGround.rect)

                ''' Collision '''
                if bun.rect.colliderect(obs1.rect) or bun.rect.colliderect(obs2.rect) or bun.rect.colliderect(obs3.rect) or bun.rect.colliderect(stage.rect):
                    bun.collide()
                    gg = True
 
                '''Pause/Unpause Music'''
                if paused == 1:
                    pygame.mixer.music.pause()

                elif paused == -1:
                    pygame.mixer.music.unpause()

                ''' Game over '''
                if gg:
                    screen.blit(youDiedText, (405,30))
                    screen.blit(restartText, (466,100))
                    bun.pauseBunny()
                    obs1.pauseObstacle()
                    obs2.pauseObstacle()
                    obs3.pauseObstacle()
                    stage.pausePlatform()
                    cloud1.pauseCloud()
                    cloud2.pauseCloud()

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
                    hsText = mainFont.render("High Score: {0}".format(highscore), 0, (0,0,0))
                    screen.blit(label, (850, 10))
                    screen.blit(hsText, (850, 40))
                    if not gg and start:
                        score += 1

                    ''' Draw objects '''
                    bun.draw(screen)
                    bunSprite.update()

                    obs1.draw(screen)
                    obs1Sprite.update()
                
                    obs2.draw(screen)
                    obs2Sprite.update()
                    
                    obs3.draw(screen)
                    obs2Sprite.update()

                    stage.draw(screen)
                    stageSprite.update()
                     
                    cloud1.draw(screen)
                    cloud1Sprite.update()

                    cloud2.draw(screen)
                    cloud2Sprite.update()

                    ''' Difficulty Levels '''
                    obs1.velocity = 10
                    obs2.velocity = 0
                    obs3.velocity = 0
                    stage.velocity = 0
                    
                    if bun.counter >= 500:
                        obs1.velocity = 11
                        obs2.velocity = 11
                        bun.lvlspeed = 4
                        
                    if bun.counter >= 1000:
                        obs1.velocity = 12
                        obs2.velocity = 12
                        stage.velocity = 12
                        bun.lvlspeed = 3

                    if bun.counter >= 1500:
                        obs1.velocity = 13
                        obs2.velocity = 13
                        obs3.velocity = 13
                        stage.velocity = 13
                        bun.lvlspeed = 2

                    if bun.counter >= 2000:
                        obs.velocity = 14
                        obs2.velocity = 14
                        obs3.velocity = 14
                        stage.velocity = 14
                        bun.lvlspeed = 1
                if not start:
                    screen.blit(titleText, (120,17))
                    screen.blit(startText, (478,478))
                    screen.blit(quitText, (473,508))
                    screen.blit(pauseText, (474, 538))

                ''' Screen update '''
                pygame.display.update()
                pygame.display.flip()

def main():
    BunnyGame()
main()
