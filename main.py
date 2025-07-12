from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.read_csv_excel import read_csv, read_excel
from src.search import process_bank_search
from src.utils import open_json


def main():
    while True:
        file_choice = input(
            """
        Привет! 
        Добро пожаловать в программу работы с банковскими транзакциями. 
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла
        """
        ).strip()
        base_path = "/Users/rybin/PycharmProjects/homework/data/"

        if file_choice == "1":  # Сравниваем со строкой
            sorted_data = open_json(f"{base_path}operations.json")
            print("Для обработки выбран JSON-файл.")
        elif file_choice == "2":
            sorted_data = read_csv(f"{base_path}transactions.csv")
            print("Для обработки выбран CSV-файл.")
        elif file_choice == "3":
            sorted_data = read_excel(f"{base_path}transactions_excel.xlsx")
            print("Для обработки выбран excel-файл.")

        while True:
            status_choice = input(
                """
            Введите статус, по которому необходимо выполнить фильтрацию. 
            Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
            """
            ).upper()

            if status_choice in ('EXECUTED', 'CANCELED', 'PENDING'):
                sorted_data = filter_by_state(sorted_data, key=status_choice)
                print(f"Операции отфильтрованы по статусу {status_choice}")
                break
            else:
                print(f'Статус операции {status_choice} недоступен.')


        date_filter = input(
            """
        Отсортировать операции по дате? Да/Нет
        """
        ).lower()

        if date_filter == "да":
            ascending_filter = input(
                """
                    Отсортировать по возрастанию или по убыванию?
                    """
            ).lower()
            if ascending_filter == "по возрастанию":
                sorted_data = sort_by_date(sorted_data, descending=False)
            elif ascending_filter == "по убыванию":
                sorted_data = sort_by_date(sorted_data, descending=True)

        filtered_by_rub = input(
            """
        Выводить только рублевые транзакции? Да/Нет
        """
        ).lower()

        if filtered_by_rub == "да":
            sorted_data = filter_by_currency(sorted_data, "RUB")

        key_word_in_description = input(
            """
        Отфильтровать список транзакций по определенному слову в описании? Да/Нет
        """
        ).lower()

        if key_word_in_description == "да":
            key_word = input(
                """
            По каким словам фильтруем?
            """
            ).lower()

            sorted_data = process_bank_search(sorted_data, key_word)

        print("Распечатываю итоговый список транзакций...")

        print(f"Всего банковских операций в выборке: {len(list(sorted_data))}")

        if len(list(sorted_data)) > 0:
            for i in sorted_data:
                print(i, end="\n")
        else:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

        break


main()
