def filter_by_currency(transactions: list[dict], code: str = "USD"):
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["name"] == code:
            yield transaction
