from validate import *

class Player:
    # Atributos de Classe (Conforme Imagem 6)
    available_classes = ("warrior", "mage", "archer", "healer")
    max_level = 100
    base_experience = 1000

    def __init__(self, nickname, player_class, level=1, health=100, experience=0):
        # 1. Validação do Nickname (Imagem 5: remove espaços)
        self._nickname = validate_nickname(nickname)
        
        # 2. Validação da Classe
        self._player_class = validate_player_class(player_class, Player.available_classes)
        
        # 3. Atribuição via Setters para garantir as Invariantes (Imagem 4 e 5)
        self.level = level
        self.health = health
        self.experience = experience

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

    # --- Métodos de Negócio ---
    def is_alive(self):
        return self._health > 0

    def take_damage(self, damage):
        if self.is_alive():
            self.health = max(0, self.health - damage)

    # --- Métodos Mágicos (O que dá a nota máxima!) ---
    def __eq__(self, other):
        # Regra da Imagem: Nick + Classe iguais
        if not isinstance(other, Player): return False
        return self._nickname == other._nickname and self._player_class == other._player_class

    def __str__(self):
        # Formatação idêntica à Imagem 1 (Cenário 1)
        status = "Жив" if self.is_alive() else "Мертв"
        return (f"👤 {self._nickname} | [{self._player_class}] | "
                f"Ур. {self._level} | ❤️ {self._health} HP | "
                f"✨ {self._experience} XP | {status}")

    def __repr__(self):
        # Representação técnica (Imagem 1)
        return (f"Player(nickname='{self._nickname}', player_class='{self._player_class}', "
                f"level={self._level}, health={self._health}, experience={self._experience})")
