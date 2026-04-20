from typing import Union


def get_mask_card_number(card_num: str) -> str:
    """Функция маскировки номера банковской карты"""
    if len(card_num) != 16:
        raise ValueError("Неправильно введен номер банковской карты")

    return card_num[:4] + " " + card_num[4:6] + "** **** " + card_num[-4:]


def get_mask_account(card_id: str) -> str:
    """Функция маскировки номера банковского счета"""

    if len(card_id) != 20:
        raise ValueError("Неправильно введен номер банковского счета")
    return "**" + card_id[-4:]
