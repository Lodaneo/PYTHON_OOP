# exceptions.py

class GameAppError(Exception):
    """Базовое исключение для всего приложения."""
    pass

class PlayerNotFoundError(GameAppError):
    """Исключение: Персонаж не найден в отряде."""
    pass

class DuplicatePlayerError(GameAppError):
    """Исключение: Персонаж с таким никнеймом уже существует."""
    pass

class InvalidDataError(GameAppError):
    """Исключение: Ошибка при обработке или формате данных."""
    pass
