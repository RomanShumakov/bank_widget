import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(dicts_list: list[dict]) -> None:
    """Проверка работоспособности функции filter_by_currency без указания валютного кода"""
    generator = filter_by_currency(dicts_list)
    assert next(generator) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(generator) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }


def test_filter_by_currency_rub(dicts_list: list[dict]) -> None:
    """Проверка работоспособности функции filter_by_currency при явном указании валютного кода"""
    generator = filter_by_currency(dicts_list, "RUB")
    assert next(generator) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(generator) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }


def test_filter_by_currency_wrong_key(dicts_list: list[dict]) -> None:
    """Проверка работоспособности функции filter_by_currency при указании несуществующего валютного кода"""
    generator = filter_by_currency(dicts_list, "empty")
    assert next(generator) == {}


def test_filter_by_currency_empty() -> None:
    """Проверка работоспособности функции filter_by_currency при передаче словаря нестандартного формата (пустого)"""
    generator = filter_by_currency([{}])
    assert next(generator) == {}


def test_transaction_descriptions(dicts_list: list[dict]) -> None:
    """Проверка работоспособности функции transaction_descriptions"""
    generator = transaction_descriptions(dicts_list)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"


def test_transaction_descriptions_empty() -> None:
    """Проверка работоспособности функции transaction_descriptions при передаче пустого словаря"""
    generator = transaction_descriptions([{}])
    assert next(generator) == {}


def test_transaction_descriptions_uncorrect_format(list_of_dicts: list[dict]) -> None:
    """Проверка работоспособности функции transaction_descriptions при передаче словаря нестандартного формата"""
    generator = transaction_descriptions(list_of_dicts)
    assert next(generator) == {}


@pytest.mark.parametrize(
    "start, stop, result",
    [(1, 5, "0000 0000 0000 0001"), (2, 5, "0000 0000 0000 0002"), (3, 5, "0000 0000 0000 0003")],
)
def test_card_number_generator_parametrize(start: int, stop: int, result: str) -> None:
    """Проверка работоспособности функции card_number_generator через параметризацию"""
    generator = card_number_generator(start, stop)
    assert next(generator) == result


def test_card_number_generator() -> None:
    """Проверка работоспособности функции card_number_generator"""
    generator = card_number_generator(10001, 10003)
    assert next(generator) == "0000 0000 0001 0001"
    assert next(generator) == "0000 0000 0001 0002"
    assert next(generator) == "0000 0000 0001 0003"
    try:
        next(generator)
    except:
        StopIteration


def test_card_number_generator_max_value() -> None:
    """Проверка работоспособности функции card_number_generator при генерации максимальных значений"""
    generator = card_number_generator(9999999999999997, 10000000000000003)
    assert next(generator) == "9999 9999 9999 9997"
    assert next(generator) == "9999 9999 9999 9998"
    assert next(generator) == "9999 9999 9999 9999"
    with pytest.raises(ValueError) as e:
        next(generator)
    assert str(e.value) == "Превышен лимит номера карты"


def test_card_number_generator_zero_value() -> None:
    """Проверка работоспособности функции card_number_generator при генерации номера, состоящего из нулей"""
    generator = card_number_generator(0, 2)
    with pytest.raises(ValueError) as e:
        next(generator)
    assert str(e.value) == "Не допустимый формат номера карты"


def test_card_number_generator_minus_value() -> None:
    """Проверка работоспособности функции card_number_generator при генерации отрицательных значений"""
    generator = card_number_generator(-2, 2)
    with pytest.raises(ValueError) as e:
        next(generator)
    assert str(e.value) == "Не допустимый формат номера карты"
