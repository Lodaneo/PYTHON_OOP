# base.py
from validate import *

class Player:
    """Базовый класс для всех сущностей игроков"""
    def __init__(self, nickname, player_class, level=1, health=100):
        self._nickname = validate_nickname(nickname)
        self._player_class = player_class
        self.level = level
        self.health = health

    @property
    def nickname(self): return self._nickname

    # Общий интерфейс для полиморфизма (Задание на 5)
    def calculate_power(self):
        """Базовый расчет силы (будет переопределен в дочерних классах)"""
        return self.level * 10

    def __str__(self):
        return f"👤 {self._nickname} | Ур. {self.level} | ❤️ {self.health} HP"
