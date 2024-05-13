import json
import os
from typing import Any
from unittest.mock import Mock, patch

from dotenv import load_dotenv

from src.utils import finance_transactions, sum_transactions


@patch("builtins.open")
def test_read_file(mock_open: Mock) -> None:
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = json.dumps(
        [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        ]
    )
    assert finance_transactions(os.path.join("..", "data", "operations.json")) == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]
    mock_open.assert_called_once_with(os.path.join("..", "data", "operations.json"), "r", encoding="utf-8")


def test_finance_transactions_false_path() -> None:
    file_operations = "C:\\Usersee\\PycharmProjects\\project_skypro\\data\\operations.json"
    assert [] == finance_transactions(file_operations)


load_dotenv()
api_token = os.getenv("API_KEY")
headers = {"apikey": api_token}
payload: dict[Any, Any] = {}


@patch("requests.get")
def test_get_currency_info_usd(mock_get: Mock) -> None:
    mock_get.return_value.json.return_value = {"conversion_rates": {"RUB": 52}}
    assert (
        sum_transactions(
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            }
        )
        == 427511.24000000005
    )
    mock_get.assert_called_once_with(
        f"https://v6.exchangerate-api.com/v6/{api_token}/latest/USD", headers=headers, data=payload
    )


@patch("requests.get")
def test_get_currency_info_eur(mock_get: Mock) -> None:
    mock_get.return_value.json.return_value = {"conversion_rates": {"RUB": 12}}
    assert (
        sum_transactions(
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "8221.37", "currency": {"name": "EUR", "code": "EUR"}},
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            }
        )
        == 98656.44
    )
    mock_get.assert_called_once_with(
        f"https://v6.exchangerate-api.com/v6/{api_token}/latest/EUR", headers=headers, data=payload
    )


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
