import pygame

class Ship:

    """Класс для управления ласточкой"""

    def __init__(self, ai_game):
        """
        Принимает аргумент класс alien_invasion
        Задает начальнгую позицию ласточке
        """
        self.screen = ai_game.screen
        # Даем доступ к настройкам
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        """Загружаю изображение  и получаю прямоугольник"""
        self.image = pygame.image.load('images/bmw.bmp')
        self.rect = self.image.get_rect()

        """Каждый новый бумер появляется у нижнего края экрана"""
        self.rect.midbottom = self.screen_rect.midbottom

        """Сохраням вещественную координату центра корабля"""
        self.x = float(self.rect.x)

        """ФЛАГ ПЕРЕМЕЩЕНИЯ"""
        self.moving_right = False
        self.moving_left = False



    def update(self):
        """Перемещает корабль вправо или влево, если клавиша нажата"""
        # Обновляем атрибут x  а не rect
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

    #     Обновляем атрибут rect чтобы машина не стояла на месте
        self.rect.x = self.x

    def blitme(self):
        """Рисуем бумер"""
        self.screen.blit(self.image, self.rect)