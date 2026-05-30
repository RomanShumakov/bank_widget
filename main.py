from src.csv_excel_readers import csv_reader, excel_reader
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.re_search import process_bank_search
from src.utils import json_reader
from src.widget import get_date, mask_account_card

if __name__ == "__main__":

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    while True:
        input_word = input("Введите значение: ")
        if input_word == "1":
            operation_data = json_reader()
            print("Для обработки выбран JSON-файл.")
            break
        elif input_word == "2":
            operation_data = csv_reader()
            print("Для обработки выбран CSV-файл.")
            break
        elif input_word == "3":
            operation_data = excel_reader()
            print("Для обработки выбран Excel-файл.")
            break
        else:
            print("Данного пункта нет в меню.")

    print("Введите статус, по которому необходимо выполнить фильтрацию.")

    while True:
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        input_word = input("Введите значение: ").upper()
        if input_word == "EXECUTED":
            filter_data = filter_by_state(operation_data, "EXECUTED")
            print('Операции отфильтрованы по статусу "EXECUTED"')
            break
        elif input_word == "CANCELED":
            filter_data = filter_by_state(operation_data, "CANCELED")
            print('Операции отфильтрованы по статусу "CANCELED"')
            break
        elif input_word == "PENDING":
            filter_data = filter_by_state(operation_data, "PENDING")
            print('Операции отфильтрованы по статусу "PENDING"')
            break
        else:
            print(f"Статус операции {input_word} недоступен.")

    while True:
        user_input = input("Отсортировать операции по дате? Да/Нет\n").lower()
        if user_input == "нет":
            time_filtered_data = filter_data
            break
        elif user_input == "да":
            input_word = input("Отсортировать по возрастанию или по убыванию?\n").lower()
            if input_word == "по возрастанию":
                time_filtered_data = sort_by_date(filter_data)
                break
            elif input_word == "по убыванию":
                time_filtered_data = sort_by_date(filter_data, False)
                break
            else:
                print("Повторите ввод: по возрастанию / по убыванию")
        else:
            print("Повторите ввод")

    while True:
        user_input = input("Выводить только рублевые транзакции? Да/Нет\n").lower()
        if user_input == "да":
            currency_data = list(filter_by_currency(time_filtered_data, "RUB"))
            break
        elif user_input == "нет":
            currency_data = time_filtered_data
            break
        else:
            print("Повторите ввод")

    while True:
        user_input = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower()
        if user_input == "да":
            transaction_word = input("Введите слово:\n").lower()
            description_filtered_data = process_bank_search(currency_data, transaction_word)
            break
        elif user_input == "нет":
            description_filtered_data = currency_data
            break
        else:
            print("Повторите ввод")

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(description_filtered_data)}")

    if len(description_filtered_data) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        for transaction in description_filtered_data:
            print(get_date(transaction["date"]), " ", transaction["description"])
            print(mask_account_card(transaction["from"]))
            print(mask_account_card(transaction["to"]))
