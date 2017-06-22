import pygame

class Background():

    def __init__(self, backgroundImage):
        pygame.sprite.Sprite.__init__(self) #Call Sprite init

        ''' Load in the background image and .get_rect it '''
        self.backgroundImage = pygame.image.load(backgroundImage)
        self.rect = self.backgroundImage.get_rect()

'''
    def scroll(self):

        if( self.x < -300 ):
            self.x = 300
        else:
            self.x -=5

    def update(self):

        screen.blit(self.backgroundImage(self.x,self.y))
'''
