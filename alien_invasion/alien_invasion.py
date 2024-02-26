import sys

import pygame


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):

        """Инициализируем игру и создаем игровые ресурсы"""

        #   инициализируем настройки для нормальной работы pygame
        pygame.init()

        #   создаем окно для игры
        self.screen = pygame.display.set_mode((1200, 800))
        #   называем окно
        pygame.display.set_caption('Инопланетное вторжение')
        # Устанавливаем цвет окна
        self.bg_color = (255, 255, 255)

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
            self.screen.fill(self.bg_color)

            # с каждым новым выполнением цикла while, стирает старый экран
            print('Стираю старый экран')
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
