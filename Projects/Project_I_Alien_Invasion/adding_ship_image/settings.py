class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1920
        self.screen_height = 1080

        # RGB colors: a mix of red, green, and blue (255, 255, 255):
        self.bg_color = (20, 20, 180)

        # Bullets limit:
        self.bullets_allowed = 5

        # This setting allow to choose from different backgrounds
        self.bg_choice = 2

        # Ship speed setting:
        self.ship_speed = 2.5
        # Limit of ships that can be used before losing:
        self.ship_limit = 3

        # Bullets settings:
        self.bullet_speed = 1.0
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (250, 0, 0)

        # Alien settings:
        self.alien_speed = 0.5
        self.fleet_drop_speed = 5
        # fleet_direction of 1 represents right; -1 represents left:
        self.fleet_direction = 1





