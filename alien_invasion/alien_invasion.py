import sys

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):

        """Инициализируем игру и создаем игровые ресурсы"""

        #   инициализируем настройки для нормальной работы pygame
        pygame.init()
        # иннициализируем settings.py с настройками
        self.settings = Settings()

        #   создаем окно для игры на весь экран
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        #   называем окно
        pygame.display.set_caption(self.settings.name_window)

        # Вызываем наш бумер и передаем туда весь класс alien
        self.ship = Ship(self)

        """Класс для хранения и управления всеми снарядами"""
        self.bullets = pygame.sprite.Group()

        """Класс для управления маслом"""
        self.aliens = pygame.sprite.Group()
        self._create_fleet()



    def run_game(self):

        """Запуск основного цикла игры"""

        while True:
            self._check_events()
            # Обновляется позиция коробля после проверки клавиатуры, но перед обновлением экрана
            self.ship.update()
            self._update_bullet()



            self._update_screen()

    def _update_bullet(self):
        """Обновляем позиции снарядов, уничтожая старые"""
        """Обновляем позицию снаряда"""
        self.bullets.update()
        """Удаление снарядов вышедших за край экрана"""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

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
                self._check_keydown_events(event)
    #             Отпустили клавишу
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)



    def _create_fleet(self):
        """Создаем флот вторжения масла амахалса и вычисляем сколько их должно быть на экране"""
        # Создаем масло
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

    #     Создаем первый ряд масла
        for alien_number in range(number_aliens_x):
    #         Создания масла и размещение его в ряду
            self._create_alien(alien_number)

    def _create_alien(self, alien_number):
            alien = Alien(self)
            alien_width = alien.rect.width
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)
    def _update_screen(self):

        """ Метод обновления изображений на экране и отображение нового экрана"""

        # перерисовывается экран в белый цвет
        # print('Крашу экран в белый цвет')
        self.screen.fill(self.settings.bg_color)

        # Рисую бумер после цикла
        self.ship.blitme()

        """Проходимся по все спрайтам и для каждого вызываем метод прорисовки"""
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        """Рисуем масло на экране"""
        self.aliens.draw(self.screen)

        # с каждым новым выполнением цикла while, стирает старый экран
        # print('Стираю старый экран')
        pygame.display.flip()


    def _check_keydown_events(self, event):
        """Метод реагирующий на нажатие клавиш"""

        if event.key == pygame.K_RIGHT:
            print('Нажали правую клавишу')
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            print('Нажали левую клавишу')
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            print('Закрываем игру')
            sys.exit()
        elif event.key == pygame.K_SPACE:
            print('Выпускаем снаряд')
            self.__fire_bullet()

    def _check_keyup_events(self, event):
        """Метод реагирующий на отпускание клавиш"""

        if event.key == pygame.K_RIGHT:
            print('Отпустиили правую клавишу')
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            print('Отпустиили левую клавишу')
            self.ship.moving_left = False

    def __fire_bullet(self):
        """Создание нового снаряда и включение его в группу снарядов"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
