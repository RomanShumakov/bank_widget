import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_num: int) -> None:
    """Функция проверяет работоспособность get_mask_card_number
    при различных вариантах ввода номера банковской карты"""
    assert get_mask_card_number(card_num) == "1234 56** **** 4321"
    assert get_mask_card_number(str(card_num)) == "1234 56** **** 4321"
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("")
    assert str(exc_info.value) == "Неправильно введен номер банковской карты"


def test_get_mask_account(card_id: int) -> None:
    """Функция проверяет работоспособность get_mask_account
    при различных вариантах ввода номера банковского счета"""
    assert get_mask_account(card_id) == "**1234"
    assert get_mask_account(str(card_id)) == "**1234"
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("")
    assert str(exc_info.value) == "Неправильно введен номер банковского счета"
