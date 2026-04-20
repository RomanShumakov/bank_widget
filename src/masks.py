from typing import Union


def get_mask_card_number(card_num: int | str) -> str:
    """Функция маскировки номера банковской карты"""
    card_id_str = str(card_num)
    if len(card_num) != 16:
        raise ValueError("Неправильно введен номер банковской карты")

    return card_id_str[:4] + " " + card_id_str[4:6] + "** **** " + card_id_str[-4:]


def get_mask_account(card_id: int | str) -> str:
    """Функция маскировки номера банковского счета"""

    card_id = str(card_id)
    if len(card_id) != 20:
        raise ValueError("Неправильно введен номер банковского счета")
    return "**" + card_id[-4:]
