import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """
    Overall class to manage game assets and behavior.
    """
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        # Set the background color.
        self.bg_color = self.settings.bg_color

    def check_events(self):
        """Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def run_the_game(self):
        """Start the main loop for the game."""
        while True:
            self.check_events()
            self.update_screen()


if __name__ == '__main__':
    # The instance to run the game.
    ai = AlienInvasion()
    ai.run_the_game()