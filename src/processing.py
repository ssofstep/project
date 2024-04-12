def new_sort_list(change_users_list: list, state='EXECUTED') -> list:
    new_users_list = []
    for i in change_users_list:
        if i["state"] == state:
            new_users_list.append(i)

    return new_users_list


def sort_dict_by_date(list_with_data: list, reverse=True) -> list:
    return sorted(list_with_data, key=lambda x: x["date"], reverse=reverse)
