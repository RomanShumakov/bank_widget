import pytest


@pytest.fixture
def card_num():
    return 1234567887654321


@pytest.fixture
def card_id():
    return 12345678876543211234


@pytest.fixture
def list_of_dicts():
    return [{"name": "MOEX", "state": "CANCELED", "date": "2026-04-20-12-00-00"},
            {"name": "MOEX", "state": "EXECUTED", "date": "2026-03-01-09-00-09"}]
