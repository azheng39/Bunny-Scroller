import pygame

class Bunny:

	def __init__(self):

		self.jumptimes = 2 #times can jump w/o ground refresh
		self.jumpup = False #is bunny allowed to jump
		self.colliding = False #is bunny colliding with obstacle

		self.x = 0 #sets position
		self.y = 0	
		self.velocity = 0 #vertical velocity is 0
		self.gravity = -10 #gravitational constant

	def jump(self):

		if (event.key == pygame.K_UP):
			
			self.jumpup = True
		
	def collide(self, enemy):

		if(self.colliding):
			
			self.velocity = 0
			print("You lost!")

	def draw(self,screen):
		
		if(self.jumpup):

			self.velocity = 20 #changes vert velocity to go up
			self.velocity += self.gravity #decreases velocity 
			self.y += self.velocity #changes position of bunny 
			
	

class Background(pygame.sprite.Sprite):

	def __init__(self,name,x,y):
		
		self.backgroundImage = pygame.image.load(name).convert_alpha()
		self.x = x	
		self.y = y
		

	def scroll(self):
		
		if self.x < -300:
			self.x = 300
		else:
			self.x -= 5
	def update(self):
		
		screen.blit(self.backgroundImage(self.x,self.y)
			    
class Obstacle:

	def __init__(self):


