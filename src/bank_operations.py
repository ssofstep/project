import re
from collections import Counter
from typing import Dict


def suitable_list(list_operations: list[dict], search_line: str) -> list[dict]:
    """Функция, которая возвращает список словарей, у которых в описании есть данная строка"""
    new_list = []
    pattern = re.compile(f"{search_line}")
    for i in list_operations:
        if pattern.search(i["description"]):
            new_list.append(i)

    return new_list


category = {
    "Перевод организации": "Перевод организации",
    "Открытие вклада": "Открытие вклада",
    "Перевод со счета на счет": "Перевод со счета на счет",
    "Перевод с карты на счет": "Перевод с карты на счет",
}


def category_dict(list_operations: list[dict], category: dict) -> dict:
    """Функция, которая возвращает словарь,где ключи — это названия категорий,
    а значения — это количество операций в каждой категории"""
    category_counts: Dict[str, int] = Counter()
    for i in list_operations:
        item_category = i["description"]
        if item_category in category:
            category_counts[item_category] += 1
    return category_counts
