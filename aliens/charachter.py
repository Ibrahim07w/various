import pygame
class Charachter:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midtop = self.screen_rect.midtop

    def blitc(self):
        self.screen.blit(self.image, self.rect)