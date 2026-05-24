from unittest.mock import patch
import requests
from src.external_api import transaction_in_rub
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY")

@patch('requests.get')
def test_transaction_in_rub_success(mock_get):
    mock_get.return_value.json.return_value = {'success': True,
                                               'query': {'from': 'USD', 'to': 'RUB', 'amount': 8221.37},
                                               'info': {'timestamp': 1779613387, 'rate': 71.790516},
                                               'date': '2026-05-24', 'result': 590216.394527}
    oper = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }
    assert transaction_in_rub(oper) == 590216.394527
    mock_get.assert_called_once_with("https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37", headers={"apikey": api_key})


@patch('requests.get')
def test_transaction_in_rub_uncorrect_payload_data(mock_get):
    mock_get.return_value.json.return_value = {}
    oper = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    }
    assert transaction_in_rub(oper) == "uncorrect payload data"
    mock_get.assert_called_once_with("https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37", headers={"apikey": api_key})


@patch('requests.get')
def test_transaction_in_rub_uncorrect_income_data(mock_get):
    mock_get.return_value.json.return_value = {'success': True,
                                               'query': {'from': 'USD', 'to': 'RUB', 'amount': 8221.37},
                                               'info': {'timestamp': 1779613387, 'rate': 71.790516},
                                               'date': '2026-05-24', 'result': 590216.394527}

    assert transaction_in_rub({}) == "uncorrect income data"

@patch('requests.get')
def test_transaction_in_rub_uncorrect_income_format(mock_get):
    mock_get.return_value.json.return_value = {'success': True,
                                               'query': {'from': 'USD', 'to': 'RUB', 'amount': 8221.37},
                                               'info': {'timestamp': 1779613387, 'rate': 71.790516},
                                               'date': '2026-05-24', 'result': 590216.394527}

    assert transaction_in_rub([]) == "uncorrect income data"
