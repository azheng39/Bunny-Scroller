import pygame

class Background(pygame.sprite.Sprite):

    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self) #Call Sprite init

        ''' Load in the background image and .get_rect it '''
        self.backgroundImage = pygame.image.load(name).convert_alpha()
        self.rect = self.backgroundImage.get_rect()
