def filter_by_state(data_list: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Функция возврата нового списка словарей с конкретным указанным значением ключа state"""
    result_list = []
    for diction in data_list:
        if diction["state"] == state:
            result_list.append(diction)
    return result_list

def sort_by_date(datatime_list: list[dict], turn_of_sort: bool = True) -> list[dict]:
    """Функция сортировки списка словарей по дате с заданием порядка сортировки"""
    return sorted(datatime_list, key=lambda date: date["date"], reverse=turn_of_sort)

