import re


def process_bank_search(data:list[dict], search:str) -> list[dict]:
    """Функция фильтрации списка транзакций по вводимой пользователем операции"""

    pattern = re.compile(search)
    return [operation for operation in data if pattern.search(operation["description"])]