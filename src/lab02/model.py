from validate import *

class Player:
    available_classes = ("warrior", "mage", "archer", "healer")
    max_level = 100
    base_experience = 1000

    def __init__(self, nickname, player_class, level=1, health=100, experience=0):
        self._nickname = validate_nickname(nickname)
        self._player_class = validate_player_class(player_class, Player.available_classes)
        self.level = level
        self.health = health
        self.experience = experience

    # --- Propriedades de Identidade ---
    @property
    def nickname(self): return self._nickname

    @property
    def player_class(self): return self._player_class

    # --- Propriedades (Getters e Setters) ---
    @property
    def level(self): return self._level
    @level.setter
    def level(self, value):
        validate_level(value, Player.max_level)
        self._level = value

    @property
    def health(self): return self._health
    @health.setter
    def health(self, value):
        validate_non_negative(value, "Здоровье")
        self._health = value

    @property
    def experience(self): return self._experience
    @experience.setter
    def experience(self, value):
        validate_non_negative(value, "Опыт")
        self._experience = value

    def is_alive(self):
        return self._health > 0

    def take_damage(self, damage):
        if self.is_alive():
            self.health = max(0, self.health - damage)

    def __eq__(self, other):
        if not isinstance(other, Player): return False
        return self._nickname == other._nickname and self._player_class == other._player_class

    def __str__(self):
        status = "Жив" if self.is_alive() else "Мертв"
        return (f"👤 {self._nickname} | [{self._player_class}] | "
                f"Ур. {self._level} | ❤️ {self._health} HP | "
                f"✨ {self._experience} XP | {status}")

    def __repr__(self):
        return (f"Player(nickname='{self._nickname}', player_class='{self._player_class}', "
                f"level={self._level}, health={self._health}, experience={self._experience})")
