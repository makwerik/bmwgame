
class Settings:

    """Класс для хранения всех настроек игры"""

    def __init__(self):

        """Настройки игры"""

        self.screen_width = 1200
        self.screen_height = 800
        # Цвет окна
        self.bg_color = (255, 255, 255)
        # Название окна
        self.name_window = 'Вторжение Маквэриков'

        # Настройка корабля
        self.ship_speed = 1.5

        """Параметры снаряда"""
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        # Максимальное число снарядов
        self.bullets_allowed = 3