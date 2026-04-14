def filter_by_state(data_list: list[dict], state='EXECUTED') -> list[dict]:
    result_list = []
    for diction in data_list:
        if diction["state"] == state:
            result_list.append(diction)
    return result_list

def sort_by_date(datatime_list: list[dict], turn_of_sort=True) -> list[dict]:
    return sorted(datatime_list, key=lambda date: date["date"], reverse=turn_of_sort)

