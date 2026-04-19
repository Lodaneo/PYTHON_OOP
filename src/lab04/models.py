# models.py
from interfaces import IPrintable, ICombatant
from base import Player # Reaproveitando do Lab anterior

class Warrior(Player, IPrintable, ICombatant):
    def __init__(self, nickname, level=1, armor=50):
        super().__init__(nickname, "warrior", level)
        self.armor = armor

    # Реализация IPrintable
    def to_string(self) -> str:
        return f"[ВОИН] {self.nickname} | Ур: {self.level} | Броня: {self.armor}"

    # Реализация ICombatant
    def execute_action(self) -> str:
        return f"⚔️ {self.nickname} совершает мощный удар мечом!"

class Mage(Player, IPrintable, ICombatant):
    def __init__(self, nickname, level=1, mana=100):
        super().__init__(nickname, "mage", level)
        self.mana = mana

    def to_string(self) -> str:
        return f"[МАГ] {self.nickname} | Ур: {self.level} | Мана: {self.mana}"

    # Реализация ICombatant
    def execute_action(self) -> str:
        return f"🪄 {self.nickname} выпускает магический поток!"
