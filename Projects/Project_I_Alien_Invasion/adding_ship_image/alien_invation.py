import sys
import pygame
from settings import Settings
from backgound import Background
from ship import Ship
from bullet import Bullet
from alien import Alien


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

        # Images used in the game:
        self.background = Background(self)
        self.ship = Ship(self)

        #  This group will be an instance of the pygame.sprite.Group class,
        #  which behaves like a list with some extra functionality that’s
        #  helpful when building games:
        self.bullets = pygame.sprite.Group()
        # Same logic but for the aliens ships:
        self.aliens = pygame.sprite.Group()
        self._crate_fleet()

        # Display game title:
        pygame.display.set_caption("Alien Invasion")
        # Set the background color/image. (Disable option at the moment)
        # self.bg_color = self.settings.bg_color

# Group for check events -----------------------------------------------------
    def _check_keydown_events(self, event):
        """Respond to key input going down (being pressed)."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        # Stop moving the ship to the left
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key input going up (being released)."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        # Stop moving the ship to the left
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

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
# -----------------------------------------------------------------------------

# Method to manage the backgrounds used in the game: --------------------------
    def _background_choice(self):
        """Calls the background image defined in the settings"""
        if self.settings.bg_choice == 1:
            self.background.blit_bg_1()
        elif self.settings.bg_choice == 2:
            self.background.blit_bg_2()

# Group for manage bullets: ---------------------------------------------------
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
# -----------------------------------------------------------------------------

# Method to manage the aliens: ------------------------------------------------
    def _crate_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien:
        alien = Alien(self)
        self.aliens.add(alien)

# Method to the screen during the game: ---------------------------------------
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # self.screen.fill(self.bg_color) (Disable option at the moment)
        # Redraw the screen during each pass through the loop: (Background + Ship image)
        self._background_choice()
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # Make the most recently drawn screen visible.
        pygame.display.flip()
# -----------------------------------------------------------------------------

# Final method that has the instances to join everything and run the game:
    def run_the_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()


if __name__ == '__main__':
    # The instance to run the game.
    ai = AlienInvasion()
    ai.run_the_game()
