# collection.py
from models import Warrior, Mage

class PlayerCollection:
    def __init__(self, name="Коллекция"):
        self.name = name
        self._items = []

    def add(self, item):
        self._items.append(item)

    # Фильтрация по типу через isinstance (Задание на 5)
    def get_only_warriors(self):
        new_col = PlayerCollection(f"Воины из {self.name}")
        for p in self._items:
            if isinstance(p, Warrior):
                new_col.add(p)
        return new_col

    def __iter__(self):
        return iter(self._items)
