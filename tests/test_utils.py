from unittest.mock import patch, mock_open
import pytest
from src.utils import json_reader

def test_json_reader_unknown_path():
    result = json_reader("unknown/path")
    assert [] == result

def test_json_reader_abs_path():
    result = json_reader("C:/Users/Temp0/PycharmProjects/testPoetryProject/data/operations.json")
    assert {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
            } in result

def test_json_reader_no_path():
    result = json_reader()
    assert {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
            } in result

@patch('builtins.open', new_callable=mock_open, read_data='')
def test_json_reader_uncorrect_data(mock_file):
    result = json_reader()
    assert result == []

@patch('builtins.open', new_callable=mock_open, read_data='[]')
def test_json_reader_no_data(mock_file):
    result = json_reader()
    assert result == []

@patch('builtins.open', new_callable=mock_open, read_data='{}')
def test_json_reader_another_type(mock_file):
    result = json_reader()
    assert result == []

@patch('builtins.open', new_callable=mock_open, read_data='[{}]')
def test_json_reader_empty_transaction(mock_file):
    result = json_reader()
    assert result == [{}]

