from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(list_of_dicts):
    assert filter_by_state(list_of_dicts, state="CANCELED") == [{"name": "MOEX", "state": "CANCELED", "date": "2026-04-20-12-00-00"}]
    assert filter_by_state(list_of_dicts) == [{"name": "MOEX", "state": "EXECUTED", "date": "2026-03-01-09-00-09"}]