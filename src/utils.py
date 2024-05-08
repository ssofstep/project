import json
from typing import Any

import requests


def finance_transactions(file_operations: str) -> Any:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о
    финансовых транзакциях или пустой список"""
    try:
        with open(file_operations, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


# print(finance_transactions("C:\\Users\Student Free\PycharmProjects\project_skypro\data\operations.json"))


def sum_transactions(transaction: dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    currency = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    headers = {"apikey": "e8d60e51fca9a55ec2011126"}
    payload: dict[Any, Any] = {}
    if currency == "USD":
        url_usd = "https://v6.exchangerate-api.com/v6/e8d60e51fca9a55ec2011126/latest/USD"
        response = requests.get(url_usd, headers=headers, data=payload)
        currency_json_usd = response.json()
        usd = currency_json_usd["conversion_rates"]["RUB"]
        rub_amount: float = usd * float(amount)
        return rub_amount
    elif currency == "EUR":
        url_eur = "https://v6.exchangerate-api.com/v6/e8d60e51fca9a55ec2011126/latest/EUR"
        response = requests.get(url_eur, headers=headers, data=payload)
        currency_json_eur = response.json()
        eur = currency_json_eur["conversion_rates"]["RUB"]
        rub_amount = eur * float(amount)
        return rub_amount
    else:
        return float(amount)
