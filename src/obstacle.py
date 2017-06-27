import pygame
import random
from ImageProcess import load_image

class Obstacle(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image('../assets/obstacle.png')
		#a = random.randrange(-32,33)
		#b = random.randrange(-32,33)
		self.rect = self.rect.inflate(45, 45)

		self.x = 1100
		self.y = 0
		self.rect.x = 1100
		self.rect.y = 415

		self.velocity = 10
		self.moving = True

	def pauseObstacle(self):
		self.moving = False

	def resumeObstacle(self):
		self.moving = True

	def reinit(self):
		self.x = 1100
		self.y = 415
		self.rect.x = 1100
		self.rect.y = 415
		self.v = 10
		self.moving = True


	def draw(self, screen):
		if(self.moving):
			if self.rect.x == -300:
				self.rect.x = 1100
			else:
				self.rect.x -= self.velocity


		screen.blit(self.image,(self.rect.x,self.rect.y))
