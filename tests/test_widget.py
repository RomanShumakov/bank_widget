from src.widget import mask_account_card, get_date
import pytest

@pytest.mark.parametrize("card_id, result", [(8765432112345678, "8765 43** **** 5678")])
def test_mask_account_card(card_id, result):
    assert mask_account_card(card_id) == result
