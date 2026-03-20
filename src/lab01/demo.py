from model import Player

# Сценарий №1 e №2: Criação e Comparação
print("--- Сценарии №1 и №2 ---")
p1 = Player("MaxVerstappen", "mage", level=10, health=200, experience=5000)
p2 = Player("MaxVerstappen", "warrior")
p3 = Player("MaxVerstappen", "mage")

print(f"Создан игрок (str):\n{p1}")
print(f"Отладочный вывод (repr):\n{repr(p1)}")
print(f"\np1 == p2? {p1 == p2} (разные классы)")
print(f"p1 == p3? {p1 == p3} (одинаковые ник и класс)\n")

# Сценарий №3: Валидация (Invariantes)
print("--- Сценарий №3 (Валидация) ---")
try:
    Player("Li", "mage") # Nickname curto demais
except ValueError as e:
    print(f"ОШИБКА (как и ожидалось): {e}")

# Сценарий №6 e №7: Atributos de Classe e Métodos de Negócio
print("\n--- Сценарии №6 и №7 (Атрибуты класса и Бой) ---")
hero = Player("CristianHorner", "warrior")
print(f"Новый герой: {hero}")

hero.take_damage(30)
print(f"После уроna 30: {hero}")

print(f"\nТекущий max_level: {Player.max_level}")
Player.max_level = 150
print(f"Изменен Player.max_level на 150")
hero.level = 150
print(f"Уровень героя теперь: {hero.level}")
