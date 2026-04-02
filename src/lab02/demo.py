from model import Player
from collection import PlayerCollection

def main():
    # Инициализация коллекции
    squad = PlayerCollection("Elite Squad")
    
    # Создание объектов (Сущностей)
    p1 = Player("MaxVerstappen", "mage", level=33, health=100)
    p2 = Player("FernandoAlonso", "warrior", level=14, health=100)
    p3 = Player("KimiRaikkonen", "archer", level=7, health=100)
    p4 = Player("LewisHamilton", "healer", level=44, health=0) # Мертвый персонаж

    # --- СЦЕНАРИЙ №1: Управление и Ограничения ---
    print("--- СЦЕНАРИЙ №1: Добавление и Дубликаты ---")
    squad.add(p1)
    squad.add(p2)
    squad.add(p3)
    squad.add(p4)
    # Попытка добавить дубликат по Nickname
    duplicate = Player("MaxVerstappen", "warrior")
    squad.add(duplicate) 
    print(f"Текущий размер коллекции (len): {len(squad)}\n")

    # --- СЦЕНАРИЙ №2: Индексация и Итерация ---
    print("--- СЦЕНАРИЙ №2: Индексация и Итерация ---")
    # Тест __getitem__
    try:
        print(f"Первый игрок в списке (index 0): {squad[0].nickname}")
        print(f"Третий игрок в списке (index 2): {squad[2].nickname}")
    except IndexError as e:
        print(e)

    # Тест __iter__ (for)
    print("Полный список отряда:")
    for player in squad:
        print(f"  -> {player}")
    print()

    # --- СЦЕНАРИЙ №3: Сортировка и Фильтрация ---
    print("--- СЦЕНАРИЙ №3: Сортировка и Фильтрация ---")
    # Сортировка по уровню
    squad.sort_by_level()
    print("Отсортировано по уровню (от макс):")
    for p in squad:
        print(f"  [{p.level}] {p.nickname}")

    # Фильтрация (Живые игроки)
    alive_squad = squad.get_alive()
    print(f"\nФильтрация: {alive_squad.name}")
    for p in alive_squad:
        print(f"  👤 {p.nickname} (HP: {p.health})")

if __name__ == "__main__":
    main()
