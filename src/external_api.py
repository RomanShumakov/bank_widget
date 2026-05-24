import requests
from dotenv import load_dotenv
import os

def transaction_in_rub(transaction):
    load_dotenv()
    api_key = os.getenv("API_KEY")
    currency = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    response = requests.get(f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}", headers={"apikey": api_key})
    return response


    # rate = response.json()['rates']['RUB']
    # amount = float(transaction['operationAmount']['amount']) * rate
    # return amount

# usd_trans = {
#     "id": 41428829,
#     "state": "EXECUTED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {
#       "amount": "8221.37",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "MasterCard 7158300734726758",
#     "to": "Счет 35383033474447895560"
#   }
# res = transaction_in_rub(usd_trans)
# print(res.text)
# print("++++++++++++++")
# print(res.json())