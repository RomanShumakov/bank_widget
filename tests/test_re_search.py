from src.re_search import process_bank_search, process_bank_operations


def test_process_bank_search(dicts_list):
    result = process_bank_search(dicts_list, "Перевод со счета на счет")
    assert result == [{
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        }
    ]

def test_process_bank_operations(dicts_list):
    result = process_bank_operations(dicts_list, ["Перевод с карты на карту", "Перевод организации"])
    assert result == {'Перевод организации': 2, 'Перевод с карты на карту': 1}
