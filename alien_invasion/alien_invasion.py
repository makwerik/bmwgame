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
            self._check_events()
            # Обновляется позиция коробля после проверки клавиатуры, но перед обновлением экрана
            self.ship.update()
            self._update_screen()



    def _check_events(self):

        """Метод для отслежнивания событий с клавиатуры и мыши"""

        # В цикле фор отслеживаем события с клавиатуры и мыши
        for event in pygame.event.get():
            print(f'Событие: {event.type}')

            if event.type == pygame.QUIT:
                print(f'Закрытие окна {event.type}')
                sys.exit()
            #Отслеживаем нажатие клавиш
            elif event.type == pygame.KEYDOWN:
                # Вправо нажали клавишу устанавливает флаг Тру и корабль перемещается вправо или влево пока не отпустят клавишу
                if event.key == pygame.K_RIGHT:
                    print('Нажали правую клавишу')
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    print('Нажали левую клавишу')
                    self.ship.moving_left = Trueфв
    #             Отпустили клавишу
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    print('Отпустиили правую клавишу')
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    print('Отпустиили левую клавишу')
                    self.ship.moving_left = False

    def _update_screen(self):

        """ Метод обновления изображений на экране и отображение нового экрана"""

        # перерисовывается экран в белый цвет
        # print('Крашу экран в белый цвет')
        self.screen.fill(self.settings.bg_color)

        # Рисую бумер после цикла
        self.ship.blitme()

        # с каждым новым выполнением цикла while, стирает старый экран
        # print('Стираю старый экран')
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
