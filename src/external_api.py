import requests
from dotenv import load_dotenv
import os

def transaction_in_rub(transaction):
    load_dotenv()
    api_key = os.getenv("API_KEY")
    response = requests.get(f"https://apilayer.com/exchangerates_data-api", headers={"Authorization": f"Bearer {api_key}"})
    rate = response.json()['rates']['RUB']
    amount = float(transaction['operationAmount']['amount']) * rate
    return amount

