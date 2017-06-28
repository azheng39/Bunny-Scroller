import pygame
from ImageProcess import load_image

class Obstacle(pygame.sprite.Sprite):

	def __init__(self):
		''' Load obstacle image and initialize it for the screen. Initialize
		variables for an obstacle object. '''
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image('../assets/obstacle.png')
		self.rect = self.rect.inflate(-20,-10)

		self.x = 1100
		self.y = 0
		self.rect.x = 1100
		self.rect.y = 415

		self.velocity = 10
		self.moving = True

	def pauseObstacle(self):
		''' Pauses movement of obstacle by setting moving equal to False. '''
		self.moving = False

	def resumeObstacle(self):
		''' Resumes movement of obstacle of setting moving equal to True. '''
		self.moving = True

	def reinit(self):
		''' Resets the obstacle to its starting state. '''
		self.x = 1100
		self.y = 415
		self.rect.x = 1100
		self.rect.y = 415
		self.velocity = 10
		self.moving = True


	def draw(self, screen):
		''' Handles the mathematics for obstacles scrolling from right to
		left of screen and resets position when off screen. Draws obstacle onto
		screen. '''
		if(self.moving):
			b = random.randrange(300,700,100)
			a = random.randrange(1100,1700,b)
			if self.rect.x <= -300:
				self.rect.x = a
			else:
				self.rect.x -= self.velocity


		screen.blit(self.image,(self.rect.x,self.rect.y))
