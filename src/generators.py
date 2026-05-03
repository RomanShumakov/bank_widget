from typing import Generator


def filter_by_currency(transactions: list[dict], code: str = "USD") -> Generator[dict]:
    """Функция возврата итератора, поочередно выдающего транзакции, где валюта операции соответствует заданной (например, USD)"""
    transaction_count = 0
    for transaction in transactions:

        if transaction == {}:
            transaction_count += 1
            yield {}
        operation_amount = transaction.get("operationAmount")
        if operation_amount:
            currency = operation_amount.get("currency")
            if currency and currency.get("code") == code:
                transaction_count += 1
                yield transaction
    if transaction_count == 0:
        yield {}


def transaction_descriptions(transactions: list[dict]) -> Generator[dict]:
    """Генераторная функция возврата описания каждой операции по очереди"""
    for transaction in transactions:
        if transaction == {}:
            yield {}
        else:
            yield transaction.get("description", {})


def card_number_generator(start: int, stop: int) -> Generator[str]:
    """Функция, генерирующая номера банковских карт  в формате XXXX XXXX XXXX XXXX"""
    begin = start
    while begin <= stop:
        result = "0000000000000000" + str(begin)
        if begin <= 0:
            raise ValueError("Не допустимый формат номера карты")
        if begin >= 10000000000000000:
            raise ValueError("Превышен лимит номера карты")

        while len(result) > 16:
            update_result = result[1:]
            result = "" + update_result
        yield result[:4] + " " + result[4:8] + " " + result[8:12] + " " + result[12:]
        begin += 1
