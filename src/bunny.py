import pygame
from ImageProcess import load_image

class Bunny(pygame.sprite.Sprite):

	def __init__(self):

		pygame.sprite.Sprite.__init__(self)
		self.bunnyImage, self.rect = load_image('../assets/0.PNG')
		self.rect = self.rect.inflate(-25, -25) #.RECT IT

		self.counter = 10
		self.imageCounter = 0

		self.jumptimes = 2 #times can jump w/o ground refresh
		self.jumpup = False #is bunny allowed to jump
		self.colliding = False #is bunny colliding with obstacle

		self.x = 0 #sets position
		self.y = 0
		self.v = -20 #vertical velocity is 0
		self.g = 1

		self.rect.x = 0
		self.rect.y = 415


	def jump(self):
		self.jumpup = True

	def collide(self, enemy):
		self.colliding = True

	def update(self):
		self.counter = self.counter + 1
		self.bunnyImage = pygame.image.load("../assets/" + str(self.imageCounter) + ".png")
		if self.counter % 5 == 0:
			self.imageCounter = self.imageCounter + 1
		if(self.imageCounter == 3):
			self.imageCounter = 0

	def draw(self,screen):
		if self.jumpup:
			self.v += self.g #Increments velocity
			self.rect.y += self.v #Changes y position

			if(self.rect.y > 415):
				self.rect.y = 415
				self.v = -20
				self.jumpup = False

		if self.colliding:
			self.colliding = False

		screen.blit(self.bunnyImage, (self.rect.x, self.rect.y))
