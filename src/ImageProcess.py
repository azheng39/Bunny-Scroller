import os
import sys
import pygame

def load_image(imageName):
    ''' Take input of image file and return image object. '''

    processingImage = pygame.image.load(imageName)
    if image.get_alpha is None:
        image = image.convert()
    else:
        image = image.convert_alpha()

    return processingImage, processingImage.get_rect()
