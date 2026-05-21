# storage.py
import json
import os
from typing import List, Dict, Any

def save(collection_data: List[Dict[str, Any]], filepath: str) -> None:
    """Сохранить данные коллекции в JSON-файл.
    
    Args:
        collection_data: Список словарей, представляющих объекты.
        filepath: Путь к файлу сохранения.
    """
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(collection_data, f, ensure_ascii=False, indent=4)

def load(filepath: str) -> List[Dict[str, Any]]:
    """Загрузить данные объектов из JSON-файла.
    
    Args:
        filepath: Путь к файлу для чтения.
        
    Returns:
        Список десериализованных словарей с данными объектов.
    """
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []
