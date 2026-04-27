# services/mapping_service.py
from typing import Dict, List, Any
from config.rules import LOOKUP, normalize
from services.validation_service import detect_type


def map_column(column: str) -> Dict[str, Any]:
    """
    Map a single column name to a canonical field using exact lookup.
    """
    key = normalize(column)

    field = LOOKUP.get(key)

    if field:
        return {
            "field": field,
            "confidence": 1.0,
            "method": "exact"
        }

    return {
        "field": None,
        "confidence": 0.0,
        "method": "none"
    }


def map_with_data(column: str, values: List[str]) -> Dict[str, Any]:
    """
    Enhanced mapping using column name + data validation.
    """
    # Step 1: try exact match
    result = map_column(column)

    if result["field"]:
        return result

    # Step 2: fallback to data-based detection
    detected = detect_type(values)

    if detected != "unknown":
        return {
            "field": detected,
            "confidence": 0.7,
            "method": "data"
        }

    return result


def map_all_columns(columns: List[str], df) -> List[Dict[str, Any]]:
    """
    Map all columns using both name and data.
    """
    results = []

    for col in columns:
        # get sample values for validation
        values = df[col].dropna().astype(str).tolist()[:50]

        mapped = map_with_data(col, values)

        results.append({
            "original": col,
            **mapped
        })

    return results