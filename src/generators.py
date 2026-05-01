def filter_by_currency(transactions: list[dict], code: str = "USD"):
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["name"] == code:
            yield transaction

def transaction_descriptions(transactions: list[dict], code: str = "USD"):
    for transaction in transactions:
        yield transaction["description"]
