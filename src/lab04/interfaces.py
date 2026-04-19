# interfaces.py
from abc import ABC, abstractmethod

class IPrintable(ABC):
    """Интерфейс для объектов, которые могут возвращать текстовое описание"""
    @abstractmethod
    def to_string(self) -> str:
        pass

class ICombatant(ABC):
    """Интерфейс для сущностей, способных участвовать в бою"""
    @abstractmethod
    def execute_action(self) -> str:
        pass
