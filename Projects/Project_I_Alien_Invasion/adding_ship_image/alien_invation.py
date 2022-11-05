import sys
import pygame
from settings import Settings
from backgound import Background
from ship import Ship


class AlienInvasion:
    """
    Overall class to manage game assets and behavior.
    """
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # Set scream size settings:
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.background = Background(self)
        self.ship = Ship(self)

        # Display game title:
        pygame.display.set_caption("Alien Invasion")
        # Set the background color/image. (Disable option at the moment)
        # self.bg_color = self.settings.bg_color

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # It's a Pygame method that watches
        # for keyboard and mouse events and store them as
        # KEYDOWN events ready to be used.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Start moving the ship to the right
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                # Stop moving the ship to the right
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key input going down (being pressed)."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        # Stop moving the ship to the left
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key input going up (being released)."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        # Stop moving the ship to the left
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _background_choice(self):
        """Calls the background image defined in the settings"""
        if self.settings.bg_choice == 1:
            self.background.blit_bg_1()
        elif self.settings.bg_choice == 2:
            self.background.blit_bg_2()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # self.screen.fill(self.bg_color) (Disable option at the moment)
        # Redraw the screen during each pass through the loop: (Background + Ship image)
        self._background_choice()
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def run_the_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()


if __name__ == '__main__':
    # The instance to run the game.
    ai = AlienInvasion()
    ai.run_the_game()
