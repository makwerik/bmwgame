import sys

import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):

        """Инициализируем игру и создаем игровые ресурсы"""

        #   инициализируем настройки для нормальной работы pygame
        pygame.init()
        # иннициализируем settings.py с настройками
        self.settings = Settings()

        #   создаем окно для игры
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #   называем окно
        pygame.display.set_caption(self.settings.name_window)

        # Вызываем наш бумер и передаем туда весь класс alien
        self.ship = Ship(self)


    def run_game(self):

        """Запуск основного цикла игры"""

        while True:
            # В цикле фор отслеживаем события с клавиатуры и мыши
            for event in pygame.event.get():
                print(f'Событие: {event.type}')

                if event.type == pygame.QUIT:
                    print(f'Закрытие окна {event.type}')
                    sys.exit()


            # перерисовывается экран в белый цвет
            print('Крашу экран в белый цвет')
            self.screen.fill(self.settings.bg_color)

            # Рисую бумер после цикла
            self.ship.blitme()

            # с каждым новым выполнением цикла while, стирает старый экран
            print('Стираю старый экран')
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
