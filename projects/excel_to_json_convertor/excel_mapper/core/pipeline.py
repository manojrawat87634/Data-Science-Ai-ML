# core/pipeline.py

from typing import Dict, Any, List

from services.excel_service import (
    read_excel,
    get_columns,
    get_preview,
    get_column_values
)
from services.mapping_service import map_column
from services.validation_service import detect_type



def serialize_value(value):
    if hasattr(value, "isoformat"):  # handles Timestamp, datetime
        return value.isoformat()
    return value


def transform_data(data, mapping):
    result = []

    for row in data:
        new_row = {}

        for m in mapping:
            if m["mapped_to"]:
                val = row.get(m["original"])
                new_row[m["mapped_to"]] = serialize_value(val)

        result.append(new_row)

    return result

def process_file(file_path: str) -> Dict[str, Any]:
    """
    Main pipeline:
    - read excel
    - extract columns
    - map columns
    - validate using data
    - return structured response
    """

    # 🔹 Step 1: Read Excel
    df = read_excel(file_path)

    # 🔹 Step 2: Get columns
    columns: List[str] = get_columns(df)

    mapping_results = []

    # 🔹 Step 3: Process each column
    for col in columns:
        # Basic mapping (rules)
        mapping = map_column(col)

        # Get sample data for validation
        values = get_column_values(df, col)

        # Detect actual data type
        detected_type = detect_type(values)

        # 🔹 Combine logic (simple version)
        if mapping["field"] is None and detected_type != "unknown":
            # fallback to detected type
            mapping["field"] = detected_type
            mapping["confidence"] = 0.6  # lower confidence

        mapping_results.append({
            "original": col,
            "mapped_to": mapping["field"],
            "confidence": mapping["confidence"],
            "detected_type": detected_type
        })

    # 🔹 Step 4: Build final JSON data (optional clean output)
    data = df.to_dict(orient="records")
    clean_data = transform_data(data, mapping_results)

    return {
    "columns": columns,
    "mapping": mapping_results,
    "clean_data": clean_data,  
}