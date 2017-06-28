import pygame
from ImageProcess import load_image
import random

class Platform(pygame.sprite.Sprite):

	def __init__(self):
		''' Load platform image and initialize it for the screen. Initialize
		variables for an platform object. '''
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image('../assets/platform.png')
		self.rect = self.rect.inflate(-10,-10)

		self.x = 1100
		self.y = 0
		self.rect.x = 1100
		self.rect.y = 370

		self.velocity = 10
		self.moving = True

	def pausePlatform(self):
		''' Pauses movement of platform by setting moving equal to False. '''
		self.moving = False

	def resumePlatform(self):
		''' Resumes movement of platform of setting moving equal to True. '''
		self.moving = True

	def reinit(self):
		''' Resets the platform to its starting state. '''
		self.x = 1100
		self.y = 370
		self.rect.x = 1100
		self.rect.y = 370
		self.velocity = 10
		self.moving = True

	def draw(self, screen):
		''' Handles the mathematics for platforms scrolling from right to
		left of screen and resets position when off screen. Draws platform onto
		screen. '''
		if(self.moving):
                        a = random.randrange(1100,1600,50)
                        if self.rect.x <= -300:
                                self.rect.x = a
                        else:
                                self.rect.x -= self.velocity


		screen.blit(self.image,(self.rect.x,self.rect.y))
