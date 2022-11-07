import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        # Load the aliens images and get its rect.
        self.alien_1 = pygame.image.load('../Images/alien_easy.bmp')
        self.rect = self.alien_1.get_rect()
        self.alien_2 = pygame.image.load('../Images/alien_medium.bmp')
        self.rect = self.alien_2.get_rect()
        self.alien_3 = pygame.image.load('../Images/alien_hard.bmp')
        self.rect = self.alien_3.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
