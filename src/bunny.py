import pygame

class Bunny():

	def __init__(self):
    	''' init bunny object '''
        pygame.sprite.Sprite.__init__(self) #sprite init
        self.bunnyImage, self.rect = load_png('') #load bunny image
        self.rect = self.rect.inflate(VALUE, VALUE) #.RECT IT
		self.counter = 10
		self.imagecounter = 0

		self.jumptimes = 2 #times can jump w/o ground refresh
		self.jumpup = False #is bunny allowed to jump
		self.colliding = False #is bunny colliding with obstacle

		self.x = 0 #sets position
		self.y = 0
		self.v = 8 #vertical velocity is 0
		self.m = -2 #mass

        self.rect.x = 0
        self.rect.y = 0


	def jump(self):
        ''' Jump boolean '''
		self.jumpup = True

	def collide(self, enemy):
        ''' Collision boolean '''
		self.colliding = True

	def update(self):
        '''Cycles through bunny images'''
		self.counter = self.counter + 1
		self.bunnyImage = load_png("../assets/" + str(self.imageCounter) + ".png")
		if self.counter % 10 == 0:
			self.imageCounter = self.imageCounter + 1
		if(self.imageCounter == 3):
			self.imageCounter = 0

	def draw(self,screen):
        '''  draws the bunny objects jump and collision '''
		if(self.jumpup):
			if(self.v>0):
				F = (0.5 * self.m * (self.v * self.v))
			else:
				F = -(0.5 * self.m * (self.v * self.v))
		self.y += -F
		self.v += -1

		if(self.y > 500):
			self.y = 500
			self.jumpup = False
			self.v = 8

        if(self.colliding):
                self.colliding = False
