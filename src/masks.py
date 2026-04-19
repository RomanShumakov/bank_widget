from typing import Union

def get_mask_card_number(card_id: Union[int, str]) -> str:
    """Функция маскировки номера банковской карты"""
    card_id_str = str(card_id)
    if len(card_id_str) == 16:
        mask_card_number = card_id_str[:4] + " " + card_id_str[4:6] + "** **** " + card_id_str[-4:]
        return mask_card_number
    else:
        return card_id_str


def get_mask_account(card_id: Union[int, str]) -> str:
    """Функция маскировки номера банковского счета"""
    card_id = str(card_id)
    if len(card_id) == 20:
        mask_account = "**" + card_id[-4:]
        return mask_account
    else:
        return card_id
