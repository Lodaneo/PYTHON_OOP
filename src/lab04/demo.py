# demo.py
from models import Warrior, Mage
from collection import PlayerCollection
from interfaces import IPrintable, ICombatant

# Универсальная функция для Сценария №2
def process_printables(items: list[IPrintable]):
    """Функция работает только с объектами, реализующими интерфейс IPrintable"""
    for item in items:
        # Полиморфизм интерфейса: вызываем метод, не зная конкретный класс
        print(item.to_string())

def main():
    # Инициализация коллекции и данных
    squad = PlayerCollection("Elite Forces")
    squad.add(Warrior("Conan", level=10, armor=50))
    squad.add(Mage("Gandalf", level=12, mana=100))

    print("="*50)
    print(" ЛАБОРАТОРНАЯ РАБОТА №4 — ДЕМОНСТРАЦИЯ ")
    print("="*50)

    # СЦЕНАРИЙ 1: Полиморфизм через интерфейс ICombatant
    # Доказывает работу через контракт поведения без условий if/else
    print("\n=== СЦЕНАРИЙ 1: Боевые действия (Интерфейс ICombatant) ===")
    combatants = squad.get_by_interface(ICombatant)
    for c in combatants:
        print(c.execute_action())

    # СЦЕНАРИЙ 2: Универсальная функция для печати
    # Доказывает использование интерфейса как типа данных
    print("\n=== СЦЕНАРИЙ 2: Универсальный отчет (Интерфейс IPrintable) ===")
    printables = squad.get_by_interface(IPrintable)
    process_printables(printables)

    # СЦЕНАРИЙ 3: Проверка множественной реализации и isinstance()
    # Доказывает, что один объект может соответствовать нескольким контрактам
    print("\n=== СЦЕНАРИЙ 3: Проверка контрактов (isinstance) ===")
    hero = squad._items[0]  # Берем первого игрока (Conan)
    print(f"Объект: {hero.nickname}")
    print(f" - Реализует IPrintable: {isinstance(hero, IPrintable)}")
    print(f" - Реализует ICombatant: {isinstance(hero, ICombatant)}")
    
    print("\n" + "="*50)
    print(" ТЕСТИРОВАНИЕ ЗАВЕРШЕНО УСПЕШНО ")
    print("="*50)

if __name__ == "__main__":
    main()
