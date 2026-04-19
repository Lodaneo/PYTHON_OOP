# CONTEÚDO DO SEU validate.py
def validate_nickname(value):
    cleaned = value.strip()
    if not (3 <= len(cleaned) <= 20):
        raise ValueError("Никнейм должен содержать от 3 до 20 символов.")
    return cleaned

def validate_player_class(value, available):
    if value.lower() not in available:
        raise ValueError(f"Неизвестный класс '{value}'. Допустимые классы: {available}")
    return value.lower()

def validate_level(val, max_lvl):
    if val < 1: raise ValueError("Уровень не может быть меньше 1.")
    if val > max_lvl: raise ValueError(f"Уровень не может превышать {max_lvl}.")

def validate_non_negative(val, name):
    if val < 0: raise ValueError(f"{name} не может быть отрицательным.")
