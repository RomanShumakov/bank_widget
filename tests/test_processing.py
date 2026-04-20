import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(list_of_dicts: list[dict]) -> None:
    """Функция тестирует поведение filter_by_state в зависсимости от различных значений state при неизменной фикстуре list_of_dicts"""
    assert filter_by_state(list_of_dicts, state="CANCELED") == [
        {"name": "MOEX", "state": "CANCELED", "date": "2026-04-20-12-00-00"},
        {"name": "AAPL", "state": "CANCELED", "date": "2025-01-20-23-00-00"},
    ]

    assert filter_by_state(list_of_dicts) == [
        {"name": "MOEX", "state": "EXECUTED", "date": "2026-03-01-09-00-09"},
        {"name": "GOLD", "state": "EXECUTED", "date": "2020-01-01-23-00-00"},
    ]


@pytest.mark.parametrize(
    "inputed, state, outputed",
    [
        (
            [
                {"name": "MOEX", "state": "CANCELED", "date": "2026-03-01-09-00-09"},
                {"name": "GOLD", "state": "EXECUTED", "date": "2020-01-01-23-00-00"},
            ],
            "EXECUTED",
            [{"name": "GOLD", "state": "EXECUTED", "date": "2020-01-01-23-00-00"}],
        ),
        ([{}], "NOTHING", []),
    ],
)
def test_filter_by_state_parametrize(inputed: list[dict], state: str, outputed: list) -> None:
    """Функция тестирует filter_by_state на соответствие входных-выходных данных"""
    assert filter_by_state(inputed, state) == outputed


def test_sort_by_date(list_of_dicts: list[dict]) -> None:
    """Функция проверяет правильность работы сортировки sort_by_date фикстуры list_of_dicts"""
    assert sort_by_date(list_of_dicts, turn_of_sort=False) == [
        {"name": "GOLD", "state": "EXECUTED", "date": "2020-01-01-23-00-00"},
        {"name": "AAPL", "state": "CANCELED", "date": "2025-01-20-23-00-00"},
        {"name": "MOEX", "state": "EXECUTED", "date": "2026-03-01-09-00-09"},
        {"name": "MOEX", "state": "CANCELED", "date": "2026-04-20-12-00-00"},
    ]

    assert sort_by_date(list_of_dicts) == [
        {"name": "MOEX", "state": "CANCELED", "date": "2026-04-20-12-00-00"},
        {"name": "MOEX", "state": "EXECUTED", "date": "2026-03-01-09-00-09"},
        {"name": "AAPL", "state": "CANCELED", "date": "2025-01-20-23-00-00"},
        {"name": "GOLD", "state": "EXECUTED", "date": "2020-01-01-23-00-00"},
    ]


def test_sort_by_date_duplicate() -> None:
    """Функция проверяет правильность сортировки sort_by_date одинаковых значений по ключу date"""
    assert sort_by_date(
        [
            {"name": "AAPL", "state": "CANCELED", "date": "2025-01-20-23-00-00"},
            {"name": "MOEX", "state": "CANCELED", "date": "2026-04-20-12-00-00"},
            {"name": "GOLD", "state": "EXECUTED", "date": "2025-01-20-23-00-00"},
        ]
    ) == [
        {"name": "MOEX", "state": "CANCELED", "date": "2026-04-20-12-00-00"},
        {"name": "AAPL", "state": "CANCELED", "date": "2025-01-20-23-00-00"},
        {"name": "GOLD", "state": "EXECUTED", "date": "2025-01-20-23-00-00"},
    ]


def test_sort_by_date_uncorrect() -> None:
    """Функция проверяет устойчивость сортировки sort_by_date некорректными форматами дат """
    assert sort_by_date(
        [
            {"name": "AAPL", "state": "CANCELED", "date": "2025-13-46-3000-00-00"},
            {"name": "MOEX", "state": "CANCELED", "date": "2026-00-12-00-00"},
            {"name": "GOLD", "state": "EXECUTED", "date": "01-20-23-00-00"},
        ]
    ) == [
        {"name": "MOEX", "state": "CANCELED", "date": "2026-00-12-00-00"},
        {"name": "AAPL", "state": "CANCELED", "date": "2025-13-46-3000-00-00"},
        {"name": "GOLD", "state": "EXECUTED", "date": "01-20-23-00-00"},
    ]
