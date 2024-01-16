import pygame
from settings import Settings


class Ship:
    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height ))
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

