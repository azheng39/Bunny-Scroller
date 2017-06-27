import os
import sys
import pygame

def load_image(name):
    ''' Take input of image file and return image object. '''

    image = pygame.image.load(name)
    if image.get_alpha is None:
        image = image.convert()
    else:
        image = image.convert_alpha()

    return image, image.get_rect()
