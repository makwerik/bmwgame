import pygame

class Ship:

    """Класс для управления ласточкой"""

    def __init__(self, ai_game):
        """
        Принимает аргумент класс alien_invasion
        Задает начальнгую позицию ласточке
        """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        """Загружаю изображение  и получаю прямоугольник"""
        self.image = pygame.image.load('images/bmw.bmp')
        self.rect = self.image.get_rect()

        """Каждый новый бумер появляется у нижнего края экрана"""
        self.rect.midbottom = self.screen_rect.midbottom

        """ФЛАГ ПЕРЕМЕЩЕНИЯ"""
        self.moving_right = False
        self.moving_left = False



    def update(self):
        """Перемещает корабль вправо или влево, если клавиша нажата"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Рисуем бумер"""
        self.screen.blit(self.image, self.rect)