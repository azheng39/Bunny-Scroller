import pygame

class Bunny():

	def __init__(self):
        ''' init kangaroo object '''
        pygame.sprite.Sprite.__init__(self) #sprite init
        self.bunnyImage, self.rect = load_png('') #load bunny image
        self.rect = self.rect.inflate(VALUE, VALUE) #.RECT IT

		self.jumptimes = 2 #times can jump w/o ground refresh
		self.jumpup = False #is bunny allowed to jump
		self.colliding = False #is bunny colliding with obstacle

		self.x = 0 #sets position
		self.y = 0
		self.velocity = 0 #vertical velocity is 0
		self.gravity = -10 #gravitational constant
        self.rect.x = 0
        self.rect.y = 0


	def jump(self):
        ''' Jump boolean '''
		self.jumpup = True

	def collide(self, enemy):
        ''' Collision boolean '''
		self.colliding = True

	def draw(self,screen):
        '''  draws the bunny objects jump and collision '''
		if(self.jumpup):

			self.velocity = 20 #changes vert velocity to go up
			self.velocity += self.gravity #decreases velocity
            self.y += self.velocity #changes position of bunny

        if(self.colliding):
                self.colliding = False
