import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Управление снарядами, выпущенными короаблём"""

    def  __init__(self, ai_game):
        """Создаем снаряды в текущей позиции корабля"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        """Создаем снаряд в позиции (0, 0) и назначаем ему правильную позицию"""

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)

        self.rect.midtop = ai_game.ship.rect.midtop

        """Позиция снаряда хранится в вещественном формате"""
        self.y = float(self.rect.y)

    def update(self):
        """Перемещение снаряда"""
        self.y -= self.settings.bullet_speed

        self.rect.y = self.y

    def draw_bullet(self):
        """Вывод снаряда на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)
