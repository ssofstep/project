import json
import os
from typing import Any

import requests
from dotenv import load_dotenv


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


load_dotenv()
api_token = os.getenv("API_KEY")


def sum_transactions(transaction: dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    currency = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    headers = {"apikey": api_token}
    payload: dict[Any, Any] = {}
    if currency == "USD":
        url_usd = f"https://v6.exchangerate-api.com/v6/{api_token}/latest/USD"
        response = requests.get(url_usd, headers=headers, data=payload)
        currency_json_usd = response.json()
        usd = currency_json_usd["conversion_rates"]["RUB"]
        rub_amount: float = usd * float(amount)
        return rub_amount
    elif currency == "EUR":
        url_eur = f"https://v6.exchangerate-api.com/v6/{api_token}/latest/EUR"
        response = requests.get(url_eur, headers=headers, data=payload)
        currency_json_eur = response.json()
        eur = currency_json_eur["conversion_rates"]["RUB"]
        rub_amount = eur * float(amount)
        return rub_amount
    else:
        return float(amount)
