# cli.py
from typing import List, Any
from app import GameController
from exceptions import GameAppError

class ConsoleApplication:
    """Слой представления интерактивного меню (CLI)."""
    
    def __init__(self) -> None:
        """Инициализация слоя CLI и подключение бизнес-контроллера."""
        self.controller: GameController = GameController()

    def run(self) -> None:
        """Запуск главного интерактивного цикла приложения."""
        print("ℹ️ Автозагрузка данных успешно выполнена.")
        while True:
            print("\n" + "="*50)
            print("       ПОЛНОФУНКЦИОНАЛЬНАЯ СИСТЕМА CLI (ЛР-7)   ")
            print("="*50)
            print("1. Показать таблицу отряда")
            print("2. Зарегистрировать Воина")
            print("3. Зарегистрировать Мага")
            print("4. Удалить персонажа из отряда")
            print("5. Сортировка отряда по стратегии")
            print("6. Фильтрация отряда по уровню")
            print("0. Сохранить изменения и Выйти")
            print("="*50)

            choice = input("Выберите пункт: ").strip()
            try:
                if choice == "1":
                    self._display_table(self.controller.get_all_players())
                elif choice == "2":
                    self._create_warrior()
                elif choice == "3":
                    self._create_mage()
                elif choice == "4":
                    self._delete_player()
                elif choice == "5":
                    self._sort_menu()
                elif choice == "6":
                    self._filter_players()
                elif choice == "0":
                    self.controller.save_to_file()
                    print("💾 Изменения сохранены. Программа успешно завершена!")
                    break
                else:
                    print("⚠️ Неверный выбор! Используйте пункты от 0 до 6.")
            except ValueError:
                print("❌ Ошибка ввода: Вместо числового значения введены символы!")
            except GameAppError as e:
                print(f"❌ Ошибка бизнес-логики: {e}")

    def _create_warrior(self) -> None:
        """Форма создания Воина."""
        name: str = input("Введите имя Воина: ").strip()
        lvl: int = int(input("Введите уровень: "))
        arm: int = int(input("Введите броню: "))
        self.controller.add_warrior(name, lvl, arm)
        print(f"✅ Воин '{name}' добавлен.")

    def _create_mage(self) -> None:
        """Форма создания Мага."""
        name: str = input("Введите имя Мага: ").strip()
        lvl: int = int(input("Введите уровень: "))
        mn: int = int(input("Введите ману: "))
        self.controller.add_mage(name, lvl, mn)
        print(f"✅ Маг '{name}' добавлен.")

    def _delete_player(self) -> None:
        """Удаление персонажа с обязательным подтверждением (Задание на 5)."""
        name: str = input("Введите имя для удаления: ").strip()
        # Сначала проверяем, существует ли он
        self.controller.find_player(name)
        
        # Подтверждение опасной операции
        confirm: str = input(f"❓ Удалить персонажа '{name}'? (y/n): ").strip().lower()
        if confirm == 'y' or confirm == 'yes':
            self.controller.remove_player(name)
            print(f"🗑️ Персонаж '{name}' успешно удален.")
        else:
            print("❌ Операция отменена пользователем.")

    def _sort_menu(self) -> None:
        """Подменю выбора стратегии сортировки (ЛР-5)."""
        print("\nСортировать по:")
        print("1. Никнейму (Алфавит)")
        print("2. Числовому уровню")
        print("3. Боевой мощности")
        opt = input("Выберите вариант: ").strip()
        
        if opt == "1":
            self.controller.sort_by_strategy("name")
        elif opt == "2":
            self.controller.sort_by_strategy("level")
        elif opt == "3":
            self.controller.sort_by_strategy("power")
        else:
            print("⚠️ Неверная стратегия сортировки.")
            return
        print("⚖️ Сортировка успешно применена к коллекции.")

    def _filter_players(self) -> None:
        """Форма фильтрации."""
        min_lvl: int = int(input("Показать персонажей уровня не ниже: "))
        res = self.controller.filter_by_min_level(min_lvl)
        self._display_table(res)

    def _display_table(self, items: List[Any]) -> None:
        """Форматированный табличный вывод (Задание на 4 и 5)."""
        if not items:
            print("ℹ️ Список объектов пуст.")
            return
        print("-" * 55)
        print(f"| {'Никнейм':<18} | {'Класс':<12} | {'Уровень':<12} |")
        print("-" * 55)
        for p in items:
            print(f"| {p.nickname:<18} | {type(p).__name__:<12} | {p.level:<12} |")
        print("-" * 55)
