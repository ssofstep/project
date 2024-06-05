import json
import os
from typing import Any

import pandas as pd
import requests
from dotenv import load_dotenv

from src.logger import setup_logger

logger = setup_logger("utils", "utils.log")


def finance_transactions(file_operations: str) -> Any:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о
    финансовых транзакциях или пустой список"""
    try:
        with open(file_operations, "r", encoding="utf-8") as file:
            data = json.load(file)
            logger.info("load json file without mistakes")
            return data
    except FileNotFoundError:
        logger.info("find FileNotFoundError")
        return []
    except json.JSONDecodeError:
        logger.info("find json.JSONDecodeError")
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
        usd = currency_json_usd.get["conversion_rates"]["RUB"]
        logger.info(f"currency rub {usd}")
        rub_amount = usd * float(amount)
        logger.info(f"amount transaction {rub_amount}")
        return float(rub_amount)
    elif currency == "EUR":
        url_eur = f"https://v6.exchangerate-api.com/v6/{api_token}/latest/EUR"
        response = requests.get(url_eur, headers=headers, data=payload)
        currency_json_eur = response.json()
        eur = currency_json_eur["conversion_rates"]["RUB"]
        logger.info(f"currency rub {eur}")
        rub_amount = eur * float(amount)
        logger.info(f"amount transaction {rub_amount}")
        return float(rub_amount)
    else:
        logger.info(f"amount transaction {amount}")
        return float(amount)


def read_csv_file(path: str) -> list:
    """Функция, которая считывает финансовые операции с CSV-файла"""
    csv_file = pd.read_csv(path, sep=";")
    csv_dict = csv_file.to_dict(orient="records")
    return csv_dict


def read_xlsx_file(path: str) -> list:
    """Функция, которая считывает финансовые операции с XLSX-файла"""
    xlsx_file = pd.read_excel(path)
    xlsx_dict = xlsx_file.to_dict(orient="records")
    return xlsx_dict
