import pygame

class Background():

    def __init__(self, name,x,y):

        self.backgroundImage = pygame.image.load(name).convert_alpha()
        self.x = x
        self.y = y
    def scroll(self):
        if self.x < -300:
            self.x = 300
        else:
            self.x -=5
    def update(self):
        screen.blit(self.backgroundImage(self.x,self.y))
