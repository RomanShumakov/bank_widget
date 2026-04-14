def filter_by_state(data_list: list[dict], state='EXECUTED') -> list[dict]:
    result_list = []
    for diction in data_list:
        if diction["state"] == state:
            result_list.append(diction)
    return result_list

