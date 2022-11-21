import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from backgound import Background
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button


class AlienInvasion:
    """
    Overall class to manage game assets and behavior.
    """
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        fullscreen = False
        if fullscreen:
            # Set scream size settings:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        else:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height

        # Images used in the game:
        self.background = Background(self)
        self.ship = Ship(self)

        # Create an instance for statistics:
        self.stats = GameStats(self)

        #  This group will be an instance of the pygame.sprite.Group class,
        #  which behaves like a list with some extra functionality that’s
        #  helpful when building games:
        self.bullets = pygame.sprite.Group()
        # Same logic but for the aliens ships:
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # Make the play button
        self.play_button = Button(self, "Play")

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

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game statistics.
            self.stats.reset_stats()
            self.stats.game_active = True
            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()
            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()
            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # It's a Pygame method that watches
        # for keyboard and mouse events and store them as
        # KEYDOWN events ready to be used.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
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
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullets and aliens that have collided"""
        # Check for any bullets that have hit aliens.
        #   If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
# -----------------------------------------------------------------------------

# Methods to control the end-game ---------------------------------------------
    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement of how many ships are left:
            self.stats.ships_left -= 1
            # Get rid of any remaining aliens and bullets:
            self.bullets.empty()
            self.aliens.empty()
            # Create a new fleet and center the ship:
            self._create_fleet()
            self.ship.center_ship()
            # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hip:
                self._ship_hit()
# -----------------------------------------------------------------------------

# Methods to manage the aliens: ------------------------------------------------
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien:
        alien = Alien(self)
        self.aliens.add(alien)
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (1 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the first row of aliens:
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number=0):
        """Create an alien and a place it in the row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """
        Check if the fleet is at an edge,
        them update the positions of all aliens in the fleet
        """
        self._check_fleet_edges()
        self.aliens.update()
        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # Look for aliens hitting the bottom of the screen:
        self._check_aliens_bottom()
# -----------------------------------------------------------------------------

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
        # Draw hte play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()
        # Make the most recently drawn screen visible.
        pygame.display.flip()
# -----------------------------------------------------------------------------

# Final method that has the instances to join everything and run the game:
    def run_the_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()


if __name__ == '__main__':
    # The instance to run the game.
    ai = AlienInvasion()
    ai.run_the_game()
