import pygame

class Background():

    def __init__(self, backgroundImage):
        pygame.sprite.Sprite.__init__(self) #Call Sprite init

        ''' Load in the background image and .get_rect it '''
        self.backgroundImage = pygame.image.load(backgroundImage).convert_alpha
        self.rect = self.backgroundImage.get_rect()
