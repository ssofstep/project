from typing import Any
from unittest.mock import patch

import requests

from src.utils import finance_transactions, sum_transactions


def test_finance_transactions_true_path() -> None:
    file_operations = "C:\\Users\\Student Free\\PycharmProjects\\project_skypro\\data\\operations.json"
    assert {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    } == finance_transactions(file_operations)[0]


def test_finance_transactions_false_path() -> None:
    file_operations = "C:\\Usersee\\PycharmProjects\\project_skypro\\data\\operations.json"
    assert [] == finance_transactions(file_operations)


def get_currency_info(currency: str) -> Any:
    response = requests.get(f"https://v6.exchangerate-api.com/v6/e8d60e51fca9a55ec2011126/latest/{currency}")
    return response.json()


def test_get_currency_info_usd() -> None:
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = 751122.4502140001
        assert get_currency_info("USD") == 751122.4502140001
        mock_get.assert_called_once_with("https://v6.exchangerate-api.com/v6/e8d60e51fca9a55ec2011126/latest/USD")


def test_get_currency_info_eur() -> None:
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = 808549.5418010001
        assert get_currency_info("EUR") == 808549.5418010001
        mock_get.assert_called_once_with("https://v6.exchangerate-api.com/v6/e8d60e51fca9a55ec2011126/latest/EUR")


def test_get_currency_info_rub() -> None:
    amount_rub = 31957.58
    assert amount_rub == sum_transactions(
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    )
