# services/excel_service.py

import pandas as pd
from typing import List, Dict, Any


def read_excel(file_path: str) -> pd.DataFrame:
    """
    Reads an Excel file and returns a cleaned DataFrame.
    """
    df = pd.read_excel(file_path)

    # Drop completely empty rows
    df = df.dropna(how="all")

    # Standardize column names (strip spaces)
    df.columns = [str(col).strip() for col in df.columns]

    return df


def get_columns(df: pd.DataFrame) -> List[str]:
    """
    Extract column names.
    """
    return df.columns.tolist()


def get_preview(df: pd.DataFrame, limit: int = 5) -> List[Dict[str, Any]]:
    """
    Return first few rows for preview (JSON format).
    """
    return df.head(limit).to_dict(orient="records")


def get_column_values(df: pd.DataFrame, column: str, limit: int = 50) -> List[str]:
    """
    Extract sample values from a column (used for validation).
    """
    if column not in df.columns:
        return []

    values = df[column].dropna().astype(str).tolist()

    return values[:limit]