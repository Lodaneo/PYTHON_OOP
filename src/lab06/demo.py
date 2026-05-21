# demo.py
import sys
import os

# Корректировка путей
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from container import TypedCollection, Displayable, Scorable

# Сущности из ЛР-3, расширенные методами протоколов без явного наследования
class Warrior:
    def __init__(self, nickname: str, level: int, armor: int) -> None:
        self.nickname: str = nickname
        self.level: int = level
        self.armor: int = armor

    # Соответствие протоколу Displayable
    def display(self) -> str:
        return f"[🛡️ ВОИН] {self.nickname} | Ур. {self.level} | Броня: {self.armor}"

    # Соответствие протоколу Scorable
    def score(self) -> float:
        return float(self.level * 1.5 + self.armor)

class Mage:
    def __init__(self, nickname: str, level: int, mana: int) -> None:
        self.nickname: str = nickname
        self.level: int = level
        self.mana: int = mana

    # Соответствие протоколу Displayable
    def display(self) -> str:
        return f"[🪄 МАГ] {self.nickname} | Ур. {self.level} | Мана: {self.mana}"

    # Соответствие протоколу Scorable
    def score(self) -> float:
        return float(self.level * 2.0 + self.mana * 0.5)


def main() -> None:
    print("="*50)
    print(" ЛАБОРАТОРНАЯ РАБОТА №6 — ДЕМОНСТРАЦИЯ  ")
    print("="*50)

    # --- СЦЕНАРИЙ 1: Работа через Protocol Displayable ---
    print("\n=== СЦЕНАРИЙ 1: Коллекция с ограничением Displayable ===")
    
    # Контейнер жестко знает, что у всех объектов внутри БУДЕТ метод .display()
    display_squad = TypedCollection[Displayable]("Выставочный Отряд")
    
    display_squad.add(Warrior("Conan", level=10, armor=40))
    display_squad.add(Mage("Gandalf", level=15, mana=120))

    # Вызываем методы протокола корректно для каждого типа без ручной проверки класса
    for item in display_squad._items:
        print(f"  Вызов метода .display(): {item.display()}")


    # --- СЦЕНАРИЙ 2: Работа через Protocol Scorable ---
    print("\n=== СЦЕНАРИЙ 2: Тот же контейнер с ограничением Scorable ===")
    
    # Один и тот же класс TypedCollection теперь работает с другим контрактом
    score_squad = TypedCollection[Scorable]("Боевой Рейтинг")
    
    score_squad.add(Warrior("Aragorn", level=12, armor=35))
    score_squad.add(Mage("Jaina", level=14, mana=90))

    # Извлекаем и выводим счет/рейтинг
    for item in score_squad._items:
        print(f"  Сущность: {getattr(item, 'nickname')} | Рейтинг (.score()): {item.score()}")

    print("\n" + "="*50)
    print(" ТЕСТИРОВАНИЕ ЗАВЕРШЕНО УСПЕШНО ")
    print("="*50)

if __name__ == "__main__":
    main()
