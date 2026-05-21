# container.py
#Для реализации строгой статической типизации, обобщенных классов (Generics) и структурных контрактов (Protocol) на этапе разработки."
from typing import TypeVar, Generic, List, Callable, Optional, Protocol, runtime_checkable

# --- 1. Определение протоколов (Задание на 5) ---

@runtime_checkable
class Displayable(Protocol):
    """Протокол для объектов, умеющих возвращать свою текстовую карточку"""
    def display(self) -> str:
        ...

@runtime_checkable
class Scorable(Protocol):
    """Протокол для объектов, имеющих числовой игровой рейтинг / боевой счет"""
    def score(self) -> float:
        ...

# --- 2. Переменные типа с ограничениями bound=  ---
T = TypeVar('T') # Универсальный TypeVar для базовых методов
D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)
R = TypeVar('R') # Для метода map

# --- 3. Универсальный типизированный контейнер ---
class TypedCollection(Generic[T]):
    """
    Обобщенная коллекция, которая может быть параметризована 
    как обычными типами, так и протоколами (ограничениями).
    """
    def __init__(self, name: str = "Главная коллекция") -> None:
        self.name: str = name
        self._items: List[T] = []

    def add(self, item: T) -> None:
        """Добавление элемента в коллекцию"""
        self._items.append(item)

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        return os_item if (os_item := next((i for i in self._items if predicate(i)), None)) else None

    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> List[R]:
        return [transform(item) for item in self._items]

    def __iter__(self) -> 'Iterator[T]':
        return iter(self._items)
