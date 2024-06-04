import re


def suitable_list(list_operations: list[dict], search_line: str) -> list[dict]:
    new_list = []
    pattern = re.compile(f"{search_line}")
    for i in list_operations:
        if pattern.search(i["description"]):
            new_list.append(i)

    return new_list


