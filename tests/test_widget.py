import pytest

from src.widget import data, masks_card_account


@pytest.mark.parametrize(
    "type_and_number, expected_result_1",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_masks_card_account(type_and_number: str, expected_result_1: str) -> None:
    assert masks_card_account(type_and_number) == expected_result_1


@pytest.mark.parametrize("data_info, expected_result_2", [("2018-07-11T02:26:18.671407", "11.07.2018")])
def test_data(data_info: str, expected_result_2: str) -> None:
    assert data(data_info) == expected_result_2
