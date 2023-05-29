class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (100, 100, 100)
# Ship settings
        self.ship_speed = 5
        self.ship_limit = 2
# Bullet settings - dark grey bullets that a re 3 pixels wide and 15
        self.bullet_speed = 5
        self.bullet_width = 10
        self.bullet_height = 30
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3
# alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 20
# fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1