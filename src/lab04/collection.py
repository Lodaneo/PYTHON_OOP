# collection.py
class PlayerCollection:
    def __init__(self, name="Main Collection"):
        self.name = name
        self._items = []

    def add(self, item):
        self._items.append(item)

    # Nota 5: Filtragem por interface usando isinstance
    def get_by_interface(self, interface_class):
        """Возвращает только те объекты, которые реализуют конкретный интерфейс"""
        return [item for item in self._items if isinstance(item, interface_class)]

    def __iter__(self):
        return iter(self._items)
