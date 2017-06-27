import pygame
import random

class Obstacle():

    def __init__(self):
        ''' init obstacle object '''
        self.image, self.rect = load_png('')
	a = random.randrange(-32,33)
	b = random.randrange(-32,33)
        self.rect = self.rect.inflate(a,b)

        self.x = 0
        self.y = 0
        self.rect.x = 0
        self.rect.y = 0

        self.velocity = 10
        self.moving = True
    def draw(self, screen):
	    ''' moves the obstacle from the right of the screen to the left '''
	    if(self.moving):
		 c = random.randrange(1100,1300,30)   
		if self.rect.x == -300:
			self.rect.x = c
		else:
			self.rect.x -= self.velocity
    def update(self):
		screen.blit(self.image,(self.rect.x,self.rect.y))
