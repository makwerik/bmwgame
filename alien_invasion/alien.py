import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Класс представляющий банку масла"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        """Загружаем изображение"""
        self.image = pygame.image.load('images/maslo.bmp')
        self.rect = self.image.get_rect()

        """Каждая новая банка масла появляется в левом верхнем углу экрана"""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        """Сохранение точной горизонтальной позиции пришельца"""
        self.x = float(self.rect.x)

