from src.widget import mask_account_card, get_date
import pytest


@pytest.mark.parametrize("card_id, result",
                         [(8765432112345678, "8765 43** **** 5678"), ("8765432112345678", "8765 43** **** 5678"),
                          ("87654321123456781111", "**1111"), ("123", "123"), (321, "321"),
                          ("", ""), ("Master Card 1111222233334444", "Master Card 1111 22** **** 4444"),
                          ("Счет 11111222223333344444", "Счет **4444")])
def test_mask_account_card(card_id, result):
    assert mask_account_card(card_id) == result
