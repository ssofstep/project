from src.utils import finance_transactions
from src.processing import filter_dict_by_state, sort_dict_by_date
import os
import re

def main():
    print('Привет! Добро пожаловать в программу работы с банковскими транзакициями. '
          'Выберите необходимый пункт меню: '
          '\n1. Получить информацию о транзакциях из json файла '
          '\n2. Получить информацию о транзакциях из csv файла '
          '\n3. Получить информацию о транзакциях из xlsx файла')
    user_input = int(input())
    if user_input == 1:
        while True:
            print('Введите статус по которому необходимо выполнить фильтрацию. '
                  '\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
            user_status = input().upper()
            if user_status in ["EXECUTED", "CANCELED", "PENDING"]:
                list_operations = finance_transactions(os.path.join('data', 'operations.json'))
                list_status = filter_dict_by_state(list_operations, user_status)
                print("Отсортировать операции по дате? Да/Нет")
                user_sort = input().lower()
                if user_sort == "да":
                    print("Отсортировать по возрастанию или по убыванию?")
                    user_reverse = input()
                    pattern = re.compile(r'возрастан')
                    user_reverse_pattern = re.findall(pattern, user_reverse)
                    list_sort = sort_dict_by_date(list_status, user_reverse_pattern)
                    print(list_sort)
                # elif user_sort == "нет":
                #
                # break
            else:
                print(f"Статус операции {user_status} недоступен.")


if __name__ == '__main__':
    main()
