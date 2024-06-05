from src.utils import finance_transactions, read_csv_file, read_xlsx_file, sum_transactions
from src.processing import filter_dict_by_state, sort_dict_by_date
from src.widget import data, masks_card_account
import os

from src.bank_operations import suitable_list


def main() -> None:
    "Функция сброки проекта"
    print('Привет! Добро пожаловать в программу работы с банковскими транзакициями. '
          'Выберите необходимый пункт меню: '
          '\n1. Получить информацию о транзакциях из json файла '
          '\n2. Получить информацию о транзакциях из csv файла '
          '\n3. Получить информацию о транзакциях из xlsx файла')
    user_input = int(input())
    if user_input == 1:
        list_operations = finance_transactions(os.path.join('data', 'operations.json'))
        print("Для обработки выбран json файл.")
    elif user_input == 2:
        list_operations = read_csv_file(os.path.join('data', 'transactions.csv'))
        print("Для обработки выбран csv файл.")
    elif user_input == 3:
        list_operations = read_xlsx_file(os.path.join('data', 'transactions_excel.xlsx'))
        print("Для обработки выбран xlsx файл.")

    while True:
        print('Введите статус по которому необходимо выполнить фильтрацию. '
              '\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
        user_status = input().upper()

        if user_status in ["EXECUTED", "CANCELED", "PENDING"]:
            list_transactions = filter_dict_by_state(list_operations, user_status)

            print("Отсортировать операции по дате? Да/Нет")

            user_sort = input().lower()

            if user_sort == "да":
                print("Отсортировать по возрастанию или по убыванию?")

                user_reverse = input().lower()

                if "возрастани" in user_reverse:
                    list_transactions = sort_dict_by_date(list_transactions)
                elif "убывани" in user_reverse:
                    list_transactions = sort_dict_by_date(list_transactions, False)

            print("Выводить только рублевые тразакции? Да/Нет")

            user_currency = input().lower()

            if user_currency == "да":
                list_currency = []

                for i in list_transactions:
                    if 'currency_code' in i.keys():
                        if i['currency_code'] == "RUB":
                            list_currency.append(i)
                    else:
                        for i in list_transactions:
                            if i["operationAmount"]["currency"]["code"] == "RUB":
                                list_currency.append(i)

            else:
                list_currency = list_transactions

            print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")

            user_suitable = input().lower()
            if user_suitable == "да":
                print("Введите строку поиска в описании")
                user_search_line = input().lower()
                list_currency = suitable_list(list_currency, user_search_line)
                print(list_currency)
            print("Распечатываю итоговый список транзакций...")

            if len(list_currency) != 0:
                print(f'Всего банковских операций в выборке: {len(list_currency)}')
                for i in list_currency:
                    date = i["date"]
                    description = i["description"]
                    account_from = i.get("from", None)
                    account_to = i["to"]
                    print(f'{data(date)} {description} ',
                          f'\n{masks_card_account(account_from)} -> {masks_card_account(account_to)}',
                          f'\nСумма: {sum_transactions(i)} руб.')

            else:
                print("Не найдено ни одной транзакции подходящей под ваши условия фильтрации")
            break
        else:
            print(f"Статус операции {user_status} недоступен.")


if __name__ == '__main__':
    main()
