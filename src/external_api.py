import requests
from dotenv import load_dotenv
import os

def transaction_in_rub(transaction):
    load_dotenv()
    api_key = os.getenv("API_KEY")
    if (type(transaction) != dict) or transaction == {}:
        return "uncorrect income data"
    if transaction.get("operationAmount") and transaction["operationAmount"].get("currency"):
        currency = transaction["operationAmount"]["currency"].get("code", "uncorrect income data")
    else:
        currency = "uncorrect income data"
    amount = transaction.get("operationAmount", {}).get("amount", "uncorrect income data")
    response = requests.get(f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}", headers={"apikey": api_key})

    total_rub_amount = response.json().get("result", "uncorrect payload data")
    return total_rub_amount
