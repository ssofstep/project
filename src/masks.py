from src.logger import setup_logger

logger = setup_logger("masks", "masks.log")


def masks_card(number_card: str) -> str:
    """Функция, которая получает номер карты и возвращает маску этой карты"""
    logger.info(f"start masks_card {number_card}")
    num1 = number_card[:4]
    num2 = number_card[4:6]
    num3 = number_card[-4:]
    result = num1 + " " + num2 + "** **** " + num3
    logger.info(f"mask {result}")
    return result


def masks_account(number_account: str) -> str:
    """Функция, которая получает номер счета и возвращает маску этого счета"""
    logger.info(f"start masks_account {number_account}")
    result = "**" + number_account[-4:]
    logger.info(f"mask {result}")
    return result
