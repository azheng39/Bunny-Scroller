import pygame
import random
from ImageProcess import load_image

class Cloud(pygame.sprite.Sprite):

	def __init__(self, num):
		''' Load cloud image and initialize it for the screen. Initialize
		variables for an cloud object. '''
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image('../assets/cloud' + str(num) + '.png')

		a = random.randrange(20,45,5)
		b = random.randrange(20,45,5)
		self.rect = self.rect.inflate(a, b)

		self.x = random.randrange(1100,1300,30)
		self.y = random.randrange(0,200,10)
		self.rect.x = random.randrange(1100,1300,30)
		self.rect.y = random.randrange(0,200,10)

		self.velocity = (num+1)/2
		self.moving = True

	def pauseCloud(self):
		''' Pauses movement of cloud by setting moving equal to False. '''
		self.moving = False

	def resumeCloud(self):
		''' Resumes movement of cloud of setting moving equal to True. '''
		self.moving = True

	def reinit(self):
		''' Resets the cloud to its starting state. '''
		self.x = random.randrange(1100,1300,30)
		self.y = random.randrange(0,200,10)
		self.rect.x = random.randrange(1100,1300,30)
		self.rect.y = random.randrange(0,200,10)
		self.velocity = (num+1)/2
		self.moving = True


	def draw(self, screen):
		''' Handles the mathematics for cloud scrolling from right to
		left of screen and resets position when off screen. Draws cloud onto
		screen. '''
		if(self.moving):
			if self.rect.x <= -500:
				self.rect.x = random.randrange(1100,1300,30)
				self.rect.y = random.randrange(0,200,10)
			else:
				self.rect.x -= self.velocity


		screen.blit(self.image,(self.rect.x,self.rect.y))
