from typing import Iterator

transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)


def filter_by_currency(transactions: list, name: str) -> Iterator:
    """Функция, которая принимает список словарей и возвращает итератор с заданной валютой"""
    for item_1 in transactions:
        if item_1["operationAmount"]["currency"]["name"] == name:
            yield item_1


obj_1 = filter_by_currency(transactions, "USD")
print(next(obj_1))
print(next(obj_1))
print(next(obj_1))


def transaction_descriptions(transactions: list) -> Iterator:
    """Функция, которая принимает список словарей и возвращает описание каждой операции по очереди"""
    for item_2 in transactions:
        yield item_2["description"]


obj_2 = transaction_descriptions(transactions)
print(next(obj_2))
print(next(obj_2))
print(next(obj_2))
print(next(obj_2))


def card_number_generator(start: int, end: int) -> Iterator:
    num = 1000_0000_0000_0000
    for i in range(start, end+1):
        num_str = str(num) + str(i)
        new_num = "0" + num_str[1:][:3] + " " + num_str[4:8] + " " + num_str[8:12] + " " + num_str[-4:]
        yield new_num

obj_3 = card_number_generator(1, 5)
print(next(obj_3))
print(next(obj_3))
print(next(obj_3))
print(next(obj_3))
print(next(obj_3))

