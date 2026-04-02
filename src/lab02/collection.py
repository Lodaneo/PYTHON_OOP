from model import Player

class PlayerCollection:
    def __init__(self, name="Главная коллекция"):
        self.name = name
        self._items = []

    # --- Методы из Задания 3 и 4 ---
    def add(self, item):
        if not isinstance(item, Player):
            raise TypeError(f"Ошибка: Ожидался Player, получено {type(item).__name__}")
        
        if any(p.nickname == item.nickname for p in self._items):
            print(f"⚠️ Ошибка: Игрок '{item.nickname}' уже существует.")
            return False

        self._items.append(item)
        return True

    def remove(self, item):
        if item in self._items:
            self._items.remove(item)
            return True
        return False

    def find_by_nickname(self, nickname):
        for p in self._items:
            if p.nickname.lower() == nickname.lower():
                return p
        return None

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    # --- Новые методы из Задания 5 (Nota 5) ---

    # 1. Индексация коллекции (collection[0])
    def __getitem__(self, index):
        if not (0 <= index < len(self._items)):
            raise IndexError("Ошибка: Индекс вне диапазона коллекции.")
        return self._items[index]

    # 2. Удаление по индексу
    def remove_at(self, index):
        if 0 <= index < len(self._items):
            removed = self._items.pop(index)
            print(f"🗑️ Удален игрок по индексу {index}: {removed.nickname}")
            return removed
        raise IndexError("Ошибка: Невозможно удалить по данному индексу.")

    # 3. Сортировка объектов (по уровню)
    def sort_by_level(self, reverse=True):
        # reverse=True для сортировки от большего к меньшему
        self._items.sort(key=lambda p: p.level, reverse=reverse)
        print(f"⚖️ Коллекция отсортирована по уровню.")

    # 4. Логические операции (Фильтрация)
    # Метод возвращает НОВУЮ коллекцию
    def get_alive(self):
        new_col = PlayerCollection(f"Живые игроки из {self.name}")
        for p in self._items:
            if p.is_alive:
                new_col.add(p)
        return new_col

    def __repr__(self):
        return f"<{self.name} | Игроков: {len(self)}>"
