import pytest

from src.masks import masks_account, masks_card


@pytest.fixture
def card() -> list:
    return ["7000792289606361", "1596837868705199", "8990922113665229"]


def test_masks_card(card: str) -> None:
    new_list_card = []
    for item in card:
        new_list_card.append(masks_card(item))
    assert new_list_card == ["7000 79** **** 6361", "1596 83** **** 5199", "8990 92** **** 5229"]


@pytest.fixture
def account() -> list:
    return ["73654108430135874305", "64686473678894779589", "11113333430135873020", "09854108430135875647"]


def test_masks_account(account: str) -> None:
    new_list_account = []
    for score in account:
        new_list_account.append(masks_account(score))
    assert new_list_account == ["**4305", "**9589", "**3020", "**5647"]
