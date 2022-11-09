import pygame
from pygame.sprite import Sprite
import random


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.alien_probability = (1, 2, 3, 4)
        self.alien_class = random.choices(self.alien_probability, weights=(60, 35, 4, 1), k=1)
        self.settings = ai_game.settings

        # Load the aliens images and get its rect.
        if self.alien_class == [1]:
            self.image = pygame.image.load('../Images/alien_easy.bmp')
            self.rect = self.image.get_rect()
        elif self.alien_class == [2]:
            self.image = pygame.image.load('../Images/alien_medium.bmp')
            self.rect = self.image.get_rect()
        elif self.alien_class == [3]:
            self.image = pygame.image.load('../Images/alien_hard.bmp')
            self.rect = self.image.get_rect()
        elif self.alien_class == [4]:
            self.image = pygame.image.load('../Images/alien_emperor.bmp')
            self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at screen edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien to the right"""
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x


