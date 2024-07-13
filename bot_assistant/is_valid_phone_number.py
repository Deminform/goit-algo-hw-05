import re


def is_valid_phone_number(phone: str) -> bool:
    return bool(re.match(r'^\+?1?\d{9,13}$', phone))
