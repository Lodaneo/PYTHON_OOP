# app.py
from typing import List, Dict, Any, Callable
import storage
from exceptions import DuplicatePlayerError, PlayerNotFoundError

class Warrior:
    """Класс Воина, перенесенный в слой моделей ЛР-7."""
    def __init__(self, nickname: str, level: int, armor: int) -> None:
        self.nickname: str = nickname
        self.level: int = level
        self.armor: int = armor

class Mage:
    """Класс Мага, перенесенный в слой моделей ЛР-7."""
    def __init__(self, nickname: str, level: int, mana: int) -> None:
        self.nickname: str = nickname
        self.level: int = level
        self.mana: int = mana

class GameController:
    """Слой бизнес-логики приложения для управления игровым отрядом."""
    
    def __init__(self, filepath: str = "game_data.json") -> None:
        """Инициализация контроллера и автозагрузка данных."""
        self.filepath: str = filepath
        self._players: List[Any] = []
        self.load_from_file()

    def add_warrior(self, nickname: str, level: int, armor: int) -> None:
        """Добавить нового Воина в отряд."""
        if self._is_duplicate(nickname):
            raise DuplicatePlayerError(f"Игрок '{nickname}' уже в отряде!")
        self._players.append(Warrior(nickname, level, armor))

    def add_mage(self, nickname: str, level: int, mana: int) -> None:
        """Добавить нового Мага в отряд."""
        if self._is_duplicate(nickname):
            raise DuplicatePlayerError(f"Игрок '{nickname}' уже в отряде!")
        self._players.append(Mage(nickname, level, mana))

    def remove_player(self, nickname: str) -> None:
        """Удалить персонажа по его никнейму."""
        player = self.find_player(nickname)
        self._players.remove(player)

    def find_player(self, nickname: str) -> Any:
        """Найти персонажа по никнейму."""
        for p in self._players:
            if p.nickname.lower() == nickname.lower():
                return p
        raise PlayerNotFoundError(f"Персонаж '{nickname}' не найден в отряде.")

    def filter_by_min_level(self, min_level: int) -> List[Any]:
        """Фильтровать персонажей по минимальному уровню."""
        return [p for p in self._players if p.level >= min_level]

    def sort_by_strategy(self, strategy_name: str) -> None:
        """Сортировать отряд динамически по выбранной стратегии (ЛР-5)."""
        strategies: Dict[str, Callable[[Any], Any]] = {
            "name": lambda p: p.nickname.lower(),
            "level": lambda p: p.level,
            "power": lambda p: getattr(p, 'calculate_power', lambda: p.level * 10)()
        }
        if strategy_name in strategies:
            self._players.sort(key=strategies[strategy_name])

    def get_all_players(self) -> List[Any]:
        """Получить текущий список всех игроков."""
        return self._players

    def save_to_file(self) -> None:
        """Сериализовать коллекцию и сохранить изменения в файл."""
        serialized_data: List[Dict[str, Any]] = []
        for p in self._players:
            data = {"nickname": p.nickname, "level": p.level, "class": type(p).__name__}
            if isinstance(p, Warrior):
                data["armor"] = p.armor
            elif isinstance(p, Mage):
                data["mana"] = p.mana
            serialized_data.append(data)
        storage.save(serialized_data, self.filepath)

    def load_from_file(self) -> None:
        """Загрузить данные из файла и восстановить объекты классов."""
        raw_data = storage.load(self.filepath)
        self._players = []
        for item in raw_data:
            if item["class"] == "Warrior":
                self._players.append(Warrior(item["nickname"], item["level"], item["armor"]))
            elif item["class"] == "Mage":
                self._players.append(Mage(item["nickname"], item["level"], item["mana"]))

    def _is_duplicate(self, nickname: str) -> bool:
        """Внутренний предикат проверки дубликатов."""
        return any(p.nickname.lower() == nickname.lower() for p in self._players)
