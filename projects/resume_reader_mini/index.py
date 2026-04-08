import re
import pdfplumber
import docx
import spacy

# load NLP model
nlp = spacy.load("en_core_web_sm")


# -----------------------------
# FILE → TEXT
# -----------------------------
def get_text(file_path):
    if file_path.endswith(".pdf"):
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    text += t + "\n"
        return text

    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        return "\n".join([p.text for p in doc.paragraphs])

    else:
        return ""


# -----------------------------
# EMAIL (STRICT)
# -----------------------------
def get_email(text):
    pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    matches = list(set(re.findall(pattern, text)))

    return matches[0] if len(matches) == 1 else None


# -----------------------------
# PHONE (STRICT)
# -----------------------------
def get_phone(text):
    pattern = r'\b(\+91[\-\s]?)?[6-9]\d{10}\b'
    matches = list(set(re.findall(pattern, text)))

    return matches[0] if len(matches) == 1 else None


# -----------------------------
# NAME (STRICT)
# -----------------------------
def get_name(text):
    lines = text.split("\n")[:5]  # top 5 lines only
    candidates = []

    for line in lines:
        doc = nlp(line)
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                candidates.append(ent.text.strip())

    candidates = list(set(candidates))

    if len(candidates) == 1:
        name = candidates[0]

        # strict filtering
        if any(char.isdigit() for char in name):
            return None
        if len(name.split()) < 2 or len(name.split()) > 4:
            return None

        return name

    return None


# -----------------------------
# MAIN
# -----------------------------
file_path = "Resume.docx"   # <-- change this to your file

text = get_text(file_path)

name = get_name(text)
email = get_email(text)
phone = get_phone(text)

print("Name:", name)
print("Email:", email)
print("Phone:", phone)