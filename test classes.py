import pygame

class Bunny:

	def __init__(self):

		self.jumptimes = 2 #times can jump w/o ground refresh
		self.jumpup = False #is bunny allowed to jump
		self.colliding = False #is bunny colliding with obstacle

		self.x = 0 #sets position
		self.y = 0	
		self.velocity = 0
		self.gravity = -10

	def jump(self):

		if (event.key == pygame.K_UP):
			
			self.jumpup = True
		
	def collide(self, enemy):



	def draw(self,screen):
		
		if(self.jumpup):

			self.velocity = 20
			self.velocity += self.gravity
			self.y += self.velocity


class Floor:

	def __init__(self):

		

class Background:

	def __init__(self):



	def scroll(self):


class Obstacle:

	def __init__(self):


