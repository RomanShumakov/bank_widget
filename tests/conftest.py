import pytest


@pytest.fixture
def card_num() -> str:
    """Фикстура для проверки номера карты в test_get_mask_card_number"""
    return "1234567887654321"


@pytest.fixture
def card_id() -> str:
    """Фикстура для проверки номера счета в get_mask_account"""
    return "12345678876543211234"


@pytest.fixture
def list_of_dicts() -> list[dict]:
    """Фикстура для проверки функций фильтрации и маскировки в processing.py"""
    return [
        {"name": "MOEX", "state": "CANCELED", "date": "2026-04-20-12-00-00"},
        {"name": "AAPL", "state": "CANCELED", "date": "2025-01-20-23-00-00"},
        {"name": "MOEX", "state": "EXECUTED", "date": "2026-03-01-09-00-09"},
        {"name": "GOLD", "state": "EXECUTED", "date": "2020-01-01-23-00-00"},
    ]
