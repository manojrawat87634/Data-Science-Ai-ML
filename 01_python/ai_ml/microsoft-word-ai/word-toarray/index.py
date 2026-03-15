import os 
import json
from docx import Document
import re

def parse_docx_sections(filepath):
    doc = Document(filepath)
    services = []
    faq = []
    about = []

    current_section = None
    current_title = None
    current_text = []
    image_counter = 1

    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue
        # print(text)
        # Section detection (case-insensitive, flexible for variations)
        if re.search(r"frequently asked questions|faq|questions and answers", text.lower(), re.IGNORECASE):
            print(text)
            current_section = "faq"
            current_title = None
            current_text = []
            continue
        elif "our services" in text.lower():
            current_section = "services"
            current_title = None
            current_text = []
            continue
        elif re.search(r"why choose|about", text.lower(), re.IGNORECASE):
            current_section = "about"
            current_title = None
            current_text = []
            continue

        # === FAQ Section ===
        if current_section == "faq":
            # Match FAQ questions like "1. Why...", "1) Why...", or "Q1: Why..."
            match = re.match(r"^\d{1,2}[\.\)]\s*(.*?)\?$", text, re.IGNORECASE) or \
                    re.match(r"^Q\d*[:\-–]?\s*(.*?)\?$", text, re.IGNORECASE)
            print(match)
            print(current_text)
            if match:
                if current_title and current_text:
                    faq.append({
                        "question": current_title.strip(),
                        "answer": " ".join(current_text).strip()
                    })
                    current_text = []
                current_title = match.group(1).strip()
            else:
                current_text.append(text)

        # === Services / About Section ===
        elif current_section in ["services", "about"]:
            if para.style.name.startswith("Heading") or text.istitle():
                if current_title and current_text:
                    entry = {
                        "title": current_title,
                        "description": " ".join(current_text).strip()
                    }
                    if current_section == "services":
                        entry["image"] = f"images/PCM Service {image_counter}.webp"
                        image_counter += 1
                        services.append(entry)
                    else:
                        about.append(entry)
                    current_text = []
                current_title = text
            else:
                current_text.append(text)

    # Final append for any remaining content
    if current_section == "faq" and current_title and current_text:
        faq.append({
            "question": current_title.strip(),
            "answer": " ".join(current_text).strip()
        })
    elif current_section in ["services", "about"] and current_title and current_text:
        entry = {
            "title": current_title,
            "description": " ".join(current_text).strip()
        }
        if current_section == "services":
            entry["image"] = f"images/ic{image_counter}.webp"
            services.append(entry)
        else:
            about.append(entry)

    return {
        "services": services,
        "faq": faq,
        "about": about
    }

def process_all_docs(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(input_folder):
        if file.endswith(".docx"):
            filepath = os.path.join(input_folder, file)
            result = parse_docx_sections(filepath)

            filename = os.path.splitext(file)[0].lower().replace(" ", "-").replace("–", "-")
            output_path = os.path.join(output_folder, f"{filename}.json")

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)


# === Set your paths ===
INPUT_FOLDER = "word_docs"
OUTPUT_FOLDER = "your_output_folder_path"