from datetime import datetime

import pytest

from src.decorators import log


@log("t.txt")
def sum_correct_filename() -> int:
    return 1 + 2


@log("t.txt")
def sum_wrong_filename() -> TypeError:
    raise TypeError


@log()
def sum_correct_without_filename() -> int:
    return 1 + 2


@log()
def sum_wrong_without_filename() -> TypeError:
    raise TypeError


@pytest.fixture
def data() -> str:
    date = str(datetime.now())[:-7]
    return date


def test_log_filename(data: str) -> None:
    sum_correct_filename()
    with open("t.txt", "r", encoding="utf8") as f:
        for i in f:
            pass
        assert i.strip() == f"{data} sum_correct_filename ok"


def test_log_without_filename(data: str) -> None:
    assert sum_correct_without_filename() == (3, f"{data} sum_correct_without_filename ok")


def test_log_filename_with_mistake(data: str) -> None:
    sum_wrong_filename()
    with open("t.txt", "r", encoding="utf8") as f:
        for i in f:
            pass
        assert i.strip() == f"{data} sum_wrong_filename error: TypeError Inputs: (), {{}}"


def test_log_without_filename_with_mistake(data: str) -> None:
    assert sum_wrong_without_filename() == f"{data} sum_wrong_without_filename error: TypeError Inputs: (), {{}}"
