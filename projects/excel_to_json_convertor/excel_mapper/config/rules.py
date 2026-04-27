# config/rules.py

from typing import Dict, List

# 🔹 Canonical field → possible column names (aliases)
RULES: Dict[str, List[str]] = {
    "name": [
        "name", "fullname", "full_name", "student_name",
        "fname", "first_name", "last_name", "full name"
    ],
    "email": [
        "email", "e_mail", "mail", "emailaddress", "email_address"
    ],
    "phone": [
        "phone", "mobile", "tel", "cell", "contact",
        "phoneno", "phone_no", "mobile_no"
    ],
    "joined_at": [
        "join", "joined", "date", "signup",
        "registration", "created", "enroll", "created_at"
    ],
    "id": [
        "id", "uid", "studentid", "student_id",
        "roll", "rollno", "roll_no"
    ],
    "age": [
        "age"
    ],
    "gender": [
        "gender", "sex"
    ],
    "address": [
        "address", "addr", "location", "street"
    ],
    "department": [
        "dept", "department", "division", "faculty"
    ],
    "course": [
        "course", "subject", "program", "programme"
    ],
}


# Normalization (shared logic)
def normalize(text: str) -> str:
    return "".join(c for c in text.lower() if c.isalnum())


#  Build reverse lookup (alias → canonical field)
def build_lookup(rules: Dict[str, List[str]]) -> Dict[str, str]:
    lookup: Dict[str, str] = {}

    for field, aliases in rules.items():
        for alias in aliases:
            lookup[normalize(alias)] = field

    return lookup


#  Precomputed lookup (import this everywhere)
LOOKUP: Dict[str, str] = build_lookup(RULES)
