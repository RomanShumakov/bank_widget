def filter_by_currency(transactions: list[dict], code: str = "USD"):
    transaction_count = 0
    for transaction in transactions:

        if transaction == {}:
            transaction_count += 1
            yield {}
        if transaction.get("operationAmount") and transaction.get("operationAmount").get(
                "currency") and transaction.get("operationAmount").get("currency").get("code") == code:
            transaction_count += 1
            yield transaction
    if transaction_count == 0:
        yield {}


def transaction_descriptions(transactions: list[dict]):
    for transaction in transactions:
        if transaction == {}:
            yield {}
        else:
            yield transaction.get("description", {})


def card_number_generator(start: int, stop: int):
    begin = start
    while begin <= stop:
        result = "0000000000000000" + str(begin)

        while len(result) > 16:
            update_result = result[1:]
            result = "" + update_result
        yield result[:4] + " " + result[4:8] + " " + result[8:12] + " " + result[12:]
        begin += 1
