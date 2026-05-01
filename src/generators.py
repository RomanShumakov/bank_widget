def filter_by_currency(transactions: list[dict], code: str = "USD"):
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == code:
            yield transaction

def transaction_descriptions(transactions: list[dict], code: str = "USD"):
    for transaction in transactions:
        yield transaction["description"]

def card_number_generator(start: int, stop: int):
    begin = start
    while begin <= stop:
        result = "0000000000000000" + str(begin)

        while len(result) > 16:
            update_result = result[1:]
            result = "" + update_result
        yield result[:4] + " " + result[4:8] + " " + result[8:12] + " " +result[12:]
        begin += 1
