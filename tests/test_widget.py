from typing import Union

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_id, result",
    [
        (8765432112345678, "8765 43** **** 5678"),
        ("8765432112345678", "8765 43** **** 5678"),
        ("87654321123456781111", "**1111"),
        ("123", "123"),
        (321, "321"),
        ("", ""),
        ("Master Card 1111222233334444", "Master Card 1111 22** **** 4444"),
        ("Счет 11111222223333344444", "Счет **4444"),
    ],
)
def test_mask_account_card(card_id: Union[int, str], result: str) -> None:
    """Функция тестирует mask_account_card с помощью параметризации нескольких входных и выходных данных"""
    assert mask_account_card(card_id) == result


def test_get_date() -> None:
    """Функция тестирует различные поведения get_date в зависсимости от различных входных данных"""
    assert get_date("2026-04-20-some_info 09:00:13") == "20.04.2026"
    with pytest.raises(ValueError) as e:
        get_date("2025-13-01")
    assert str(e.value) == "Недопустимае данные для даты"
    with pytest.raises(ValueError) as e:
        get_date("roll-in-bed")
    assert str(e.value) == "Недопустимый формат ввода"
