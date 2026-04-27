# services/validation_service.py

import re
from typing import List


def is_email(value: str) -> bool:
    return bool(re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", value))


def is_phone(value: str) -> bool:
    return bool(re.match(r"^[0-9]{10}$", value))


def is_date(value: str) -> bool:
    # simple check (can improve later)
    return bool(re.match(r"\d{4}-\d{2}-\d{2}", value))


def is_numeric(value: str) -> bool:
    return value.isdigit()


#  Main detection function
def detect_type(values: List[str]) -> str:
    """
    Detect the type of a column based on sample values.
    """

    # Clean values
    values = [v.strip() for v in values if v and str(v).strip()]

    if not values:
        return "unknown"

    total = len(values)

    email_count = sum(1 for v in values if is_email(v))
    phone_count = sum(1 for v in values if is_phone(v))
    date_count = sum(1 for v in values if is_date(v))
    numeric_count = sum(1 for v in values if is_numeric(v))

    #  Calculate ratios
    email_ratio = email_count / total
    phone_ratio = phone_count / total
    date_ratio = date_count / total
    numeric_ratio = numeric_count / total

    #  Decision logic (threshold based)
    if email_ratio > 0.8:
        return "email"

    if phone_ratio > 0.8:
        return "phone"

    if date_ratio > 0.8:
        return "joined_at"

    if numeric_ratio > 0.9:
        return "age"  # basic assumption

    return "unknown"