import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):
        '''Init Alien'''
        super().__init__()
        self.screen = ai_game.screen

        # Load image of alien
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # New Alien appear in lef-upper corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

