class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        # RGB colors: a mix of red, green, and blue (255, 255, 255):
        self.bg_color = (20, 20, 180)
        # This setting allow to choose from different backgrounds
        self.bg_choice = 2
        # Ship speed setting:
        self.ship_speed = 1.5
