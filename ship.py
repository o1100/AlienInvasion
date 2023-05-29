import pygame
class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
# Load the ship image and gets its rectangle
        self.image = pygame.image.load('rocket.png')
        self.rect = self.image.get_rect()
# Start each new ship at the bottom of the center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
#Store a decimal value fo the ship's horizontal position.
        self.x = float(self.rect.x)
#Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left >0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)