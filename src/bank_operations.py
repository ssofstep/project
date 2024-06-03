import re


def suitable_list(list_operations: list[dict], search_line: str) -> list[dict]:
    new_list = []
    for i in list_operations:
        if search_line in i.keys():
            new_list.append(i)

    return new_list


