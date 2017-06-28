import pygame
from ImageProcess import load_image

class Bunny(pygame.sprite.Sprite):

	def __init__(self):
		'''  Load bunny image and initialize it for the screen. Initialize
		variables for a bunny object. '''
		pygame.sprite.Sprite.__init__(self)
		self.bunnyImage, self.rect = load_image('../assets/0.png')
		self.rect = self.rect.inflate(-5,-7) #.RECT IT

		self.counter = 10
		self.imageCounter = 0

		self.jumptimes = 2 #times can jump w/o ground refresh
		self.jumpup = False #is bunny allowed to jump
		self.colliding = False #is bunny colliding with obstacle

		self.x = 0 #sets position
		self.y = 0
		self.rect.x = 100
		self.rect.y = 415
		
		self.v = -20 #vertical velocity is 0
		self.g = 1

	def jump(self):
		''' Set jumpup equal to True. '''
		self.jumpup = True

	def collide(self):
		''' Set colliding equal to True. '''
		self.colliding = True

	def update(self):
		''' Handles the animation of the bunny running. '''
		self.counter = self.counter + 1
		self.bunnyImage = pygame.image.load("../assets/" + str(self.imageCounter) + ".png")
		if self.counter % 5 == 0:
			self.imageCounter = self.imageCounter + 1
		if(self.imageCounter == 3):
			self.imageCounter = 0

	def pauseBunny(self):
		'''	Pauses bunny: Set counter equal to 0 to stop running animation.
		Set jumpup equal to False to stop bunny from jumping. '''
		self.counter = 0
		self.jumpup = False

	def resumeBunny(self):
		''' Resumes bunny.Resumes bunny movement by allowing it to jump again. '''
		self.jumpup = True

	def reinit(self):
		''' Resets the bunny to its starting state. '''
		self.x = 0
		self.y = 0
		#self.v = -20
		self.rect.x = 100
		self.rect.y = 415

	def draw(self,screen):
		''' Handles jumping mathematics and draws the bunny onto the screen. Resets
		colliding variable to False if colliding. '''
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
