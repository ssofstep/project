from src.masks import masks_card, masks_account

def masks_card_account(type_and_number: str) -> str:
    """Функция, которая принимает на вход строку информацией тип карты/счета и номер карты/счета и возвращает маску"""
    name = "".join([n for n in type_and_number if n.isalpha() or n == " "]).strip()
    number = "".join([num for num in type_and_number if num.isdigit()])
    if name != "Счет":
        card = masks_card(number)
        return f"{name} {card}"
    elif name == "Счет":
        account = masks_account(number)
        return f"{name} {account}"


def data(data_info: str) -> str:
    """Функция, которая принимает на вход строку с информацией о дне и возвращает дату"""
    now_data = data_info[:10]
    num_list = now_data.split("-")

    return ".".join(num_list[::-1])

