def filter_dict_by_state(change_users_list: list, state: str = "EXECUTED") -> list:
    """Функция, которая принимает список словарей и возвращает новый список, у которых ключ state"""
    new_users_list = []
    for i in change_users_list:
        if i.get("state") == state:
            new_users_list.append(i)

    return new_users_list


def sort_dict_by_date(list_with_data: list, reverse: bool = True) -> list:
    """Функция, которая принимает на вход список словарей и возвращает новый список,
    в котором исходные словари отсортированы по убыванию даты"""
    return sorted(list_with_data, key=lambda x: x["date"], reverse=reverse)
