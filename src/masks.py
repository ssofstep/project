def masks_card(number_card: str) -> str:
    """Функция, которая получает номер карты и возвращает маску этой карты"""
    num1 = number_card[:4]
    num2 = number_card[4:6]
    num3 = number_card[-4:]
    return num1 + " " + num2 + "** **** " + num3


def masks_account(number_account: str) -> str:
    """Функция, которая получает номер счета и возвращает маску этого счета"""
    return "**" + number_account[-4:]
