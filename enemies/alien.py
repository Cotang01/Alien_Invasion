import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, my_game):
        super().__init__()
        self.screen = my_game.screen
        self.settings = my_game.settings

        self.image = pygame.image.load('images/enemy_1.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def update(self):
        """ Перемещение пришельца """
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """ Проверка, упёрся ли флот в край экрана """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

