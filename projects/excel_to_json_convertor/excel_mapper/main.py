# main.py

import json
from core.pipeline import process_file


def main():
    file_path = "student.xlsx"

    try:
        result = process_file(file_path)

        print("\n=== FULL JSON OUTPUT ===")
        print(json.dumps(result, indent=2))

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()