
def get_mask_card_number(card_id: int) -> str:
    """Функция маскировки номера банковской карты"""
    card_id_str = str(card_id)
    mask_card_number = card_id_str[:4] + " " + card_id_str[4:6] + "** **** " + card_id_str[-4:]

    return mask_card_number


def get_mask_account(card_id: int) -> str:
    """Функция маскировки номера банковского счета"""
    mask_account = "**" + (str(card_id))[-4:]

    return mask_account
