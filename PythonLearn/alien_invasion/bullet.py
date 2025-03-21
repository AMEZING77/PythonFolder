import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game, direction):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.direction = direction

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullets"""
        if self.direction == 'w':
            self.update_w()
        elif self.direction == 'a':
            self.update_a()
        elif self.direction == 's':
            self.update_s()
        elif self.direction == 'd':
            self.update_d()

    def update_w(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def update_a(self):
        """Move the bullet left the screen."""
        # Update the decimal position of the bullet.
        self.x -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.x = self.x

    def update_s(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y += self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def update_d(self):
        """Move the bullet left the screen."""
        # Update the decimal position of the bullet.
        self.x += self.settings.bullet_speed
        # Update the rect position.
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
