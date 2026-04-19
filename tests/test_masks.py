import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(card_num):
    assert get_mask_card_number(card_num) == "1234 56** **** 4321"
    assert get_mask_card_number(str(card_num)) == "1234 56** **** 4321"
    assert get_mask_card_number(54321) == "54321"
    assert get_mask_card_number("") == ""



def test_get_mask_account(card_id):
    assert get_mask_account(card_id) == "**1234"
    assert get_mask_account(str(card_id)) == "**1234"
    assert get_mask_account(12345) == "12345"
    assert get_mask_account("") == ""