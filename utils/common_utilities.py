import re
from decimal import Decimal


def extract_and_convert_to_decimal(price_str):
    cleaned_str = re.sub(r'[a-zA-Z\s]', '', price_str)
    cleaned_str = re.sub(r'[^0-9.]', '', cleaned_str)
    price_decimal = Decimal(cleaned_str)
    return price_decimal
