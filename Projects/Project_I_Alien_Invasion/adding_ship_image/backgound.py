import pygame


class Background:
    """A class to allow choosing from different backgrounds..."""

    def __init__(self, ai_game):
        """Load the images for different backgrounds."""
        self.screen = ai_game.screen
        # Load the backgrounds images and get its rect.
        self.bg_image_1 = pygame.image.load('../Images/galaxy_background_1.bmp')
        self.bg_image_2 = pygame.image.load('../Images/galaxy_background_2.bmp')

    def blit_bg_1(self):
        """Draw the background number 1."""
        self.screen.blit(self.bg_image_1, (0, 0))

    def blit_bg_2(self):
        """Draw the background number 2."""
        self.screen.blit(self.bg_image_2, (0, 0))
