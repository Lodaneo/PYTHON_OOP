# models.py
from base import Player
from validate import validate_non_negative

class Warrior(Player):
    """Воин: специализируется на броне и физической силе"""
    def __init__(self, nickname, level=1, health=150, armor=50):
        super().__init__(nickname, "warrior", level, health)
        self.armor = armor

    # Переопределение метода (Полиморфизм - Задание на 4 и 5)
    def calculate_power(self):
        return (self.level * 10) + self.armor

    # Новый метод (Задание на 3)
    def use_shield(self):
        return f"🛡️ {self.nickname} блокирует удар щитом!"

    def __str__(self):
        return super().__str__() + f" | 🛡️ Броня: {self.armor}"

class Mage(Player):
    """Маг: специализируется на мане и заклинаниях"""
    def __init__(self, nickname, level=1, health=80, mana=100):
        super().__init__(nickname, "mage", level, health)
        self.mana = mana

    def calculate_power(self):
        return (self.level * 10) + (self.mana // 2)

    def cast_spell(self):
        return f"🪄 {self.nickname} запускает огненный шар!"

    def __str__(self):
        return super().__str__() + f" | 🪄 Мана: {self.mana}"
