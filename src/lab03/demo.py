# demo.py
from models import Warrior, Mage
from collection import PlayerCollection

def main():
    # Создаем общую коллекцию (Задание на 4)
    squad = PlayerCollection("Элитный Отряд")
    squad.add(Warrior("Conan", level=15, armor=60))
    squad.add(Mage("Gandalf", level=20, mana=200))
    squad.add(Warrior("Aragorn", level=18, armor=45))

    # СЦЕНАРИЙ 1: Полиморфизм (Задание на 5 - Без IF)
    print("--- Сценарий 1: Общий интерфейс (calculate_power) ---")
    for p in squad:
        print(f"Игрок: {p.nickname} -> Боевая мощь: {p.calculate_power()}")

    # СЦЕНАРИЙ 2: Проверка типов (Задание на 4)
    print("\n--- Сценарий 2: Использование isinstance() ---")
    for p in squad:
        if isinstance(p, Warrior):
            print(f"{p.nickname}: {p.use_shield()}")
        elif isinstance(p, Mage):
            print(f"{p.nickname}: {p.cast_spell()}")

    # СЦЕНАРИЙ 3: Фильтрация коллекции (Задание на 5)
    print("\n--- Сценарий 3: Выборка только воинов ---")
    warriors = squad.get_only_warriors()
    for w in warriors:
        print(w)

if __name__ == "__main__":
    main()
