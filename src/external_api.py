import requests
from dotenv import load_dotenv
import os

def transaction_in_rub(transaction):
    load_dotenv()
    api_key = os.getenv("API_KEY")
    currency = transaction.get("operationAmount").get("currency").get("code")
    amount = transaction.get("operationAmount").get("amount")
    response = requests.get(f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}", headers={"apikey": api_key})

    total_rub_amount = response.json().get("result")
    return total_rub_amount
