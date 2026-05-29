import re
from collections import Counter


def process_bank_search(data:list[dict], search:str) -> list[dict]:
    """Функция фильтрации списка транзакций по вводимой пользователем операции"""

    pattern = re.compile(search)
    return [operation for operation in data if pattern.search(operation["description"])]


def process_bank_operations(data:list[dict], categories:list)->dict:
    """Функция возврата колличества операций по каждой указанной категории на основе списка банковских операций"""

    return dict(Counter([operation["description"] for operation in data if operation["description"] in categories]))
