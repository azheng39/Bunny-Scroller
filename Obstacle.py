import pygame

class Obstacle():

    def __init__(self):
        self.image, self.rect = load_png('')
        self.rect = self.rect.inflate(0, 0)

        self.x = 0
        self.y = 0
        self.rect.x = 0
        self.rect.y = 0

        self.velocity = 0
        self.moving = True

    def draw(self, screen):
        ''' moves the obstacle from the right of the screen to the left '''
        if(self.moving):
            
