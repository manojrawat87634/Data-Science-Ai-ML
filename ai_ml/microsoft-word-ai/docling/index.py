from docling.document_converter import DocumentConverter
import json

converter = DocumentConverter()
# Convert a single .docx
conv_result = converter.convert("m.docx")
doc = conv_result.document

doc_json = doc.export_to_dict()

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(doc_json, f, indent=2)

print("✅ Document converted and saved to output.json")


import json

# Load the JSON file
with open("output.json", "r", encoding="utf-8") as f:
    doc_json = json.load(f)

# Initialize output structures
faqs = []
why_choose_us = []
other_content = []

# Helper function to get text by self_ref
def get_text_by_ref(ref, texts):
    for text in texts:
        if text["self_ref"] == ref:
            return text
    return None

# Helper function to get group by self_ref
def get_group_by_ref(ref, groups):
    for group in groups:
        if group["self_ref"] == ref:
            return group
    return None

# Extract FAQs
faq_section = get_text_by_ref("#/texts/44", doc_json["texts"])
if faq_section:
    faq_data = {"section_title": faq_section["text"], "items": []}
    for group_ref in faq_section["children"]:
        if group_ref["$ref"].startswith("#/groups"):
            group = get_group_by_ref(group_ref["$ref"], doc_json["groups"])
            if group and len(group["children"]) == 2:  # Expecting question and answer
                question = get_text_by_ref(group["children"][0]["$ref"], doc_json["texts"])
                answer = get_text_by_ref(group["children"][1]["$ref"], doc_json["texts"])
                if question and answer:
                    faq_data["items"].append({
                        "question": question["text"],
                        "answer": answer["text"]
                    })
    faqs.append(faq_data)

# Extract Why Choose Us
why_choose_section = get_text_by_ref("#/texts/24", doc_json["texts"])
if why_choose_section:
    why_choose_data = {"section_title": why_choose_section["text"], "items": []}
    for child_ref in why_choose_section["children"]:
        child_text = get_text_by_ref(child_ref["$ref"], doc_json["texts"])
        if child_text and child_text["label"] == "section_header" and child_text["level"] == 3:
            # Find the paragraph under this header
            for sub_child_ref in child_text["children"]:
                sub_child_text = get_text_by_ref(sub_child_ref["$ref"], doc_json["texts"])
                if sub_child_text and sub_child_text["label"] == "paragraph":
                    why_choose_data["items"].append({
                        "title": child_text["text"],
                        "description": sub_child_text["text"]
                    })
    why_choose_us.append(why_choose_data)

# Extract Other Content
# Main introduction (texts[2, 3, 4, 5] under texts[0])
main_section = get_text_by_ref("#/texts/0", doc_json["texts"])
if main_section:
    main_content = {"section_title": main_section["text"], "paragraphs": []}
    for child_ref in main_section["children"]:
        child_text = get_text_by_ref(child_ref["$ref"], doc_json["texts"])
        if child_text and child_text["label"] == "paragraph" and child_text["text"]:
            main_content["paragraphs"].append(child_text["text"])
    other_content.append(main_content)

# Our Piano Removal Services (texts[6] and its subsections)
services_section = get_text_by_ref("#/texts/6", doc_json["texts"])
if services_section:
    services_content = {"section_title": services_section["text"], "subsections": []}
    for child_ref in services_section["children"]:
        child_text = get_text_by_ref(child_ref["$ref"], doc_json["texts"])
        if child_text and child_text["label"] == "section_header" and child_text["level"] == 3:
            # Find the paragraph under this header
            for sub_child_ref in child_text["children"]:
                sub_child_text = get_text_by_ref(sub_child_ref["$ref"], doc_json["texts"])
                if sub_child_text and sub_child_text["label"] == "paragraph":
                    services_content["subsections"].append({
                        "title": child_text["text"],
                        "description": sub_child_text["text"]
                    })
    other_content.append(services_content)

# Combine all formatted data
formatted_output = {
    "faqs": faqs,
    "why_choose_us": why_choose_us,
    "other_content": other_content
}

# Save formatted output to a new JSON file
with open("formatted_output.json", "w", encoding="utf-8") as f:
    json.dump(formatted_output, f, indent=2)

# Print a sample of the output for verification
print("FAQs:")
for faq in faqs:
    print(f"Section: {faq['section_title']}")
    for item in faq["items"]:
        print(f"  Q: {item['question']}")
        print(f"  A: {item['answer']}\n")

print("Why Choose Us:")
for section in why_choose_us:
    print(f"Section: {section['section_title']}")
    for item in section["items"]:
        print(f"  Title: {item['title']}")
        print(f"  Description: {item['description']}\n")

print("Other Content:")
for section in other_content:
    print(f"Section: {section['section_title']}")
    if "paragraphs" in section:
        for para in section["paragraphs"]:
            print(f"  Paragraph: {para}\n")
    if "subsections" in section:
        for subsection in section["subsections"]:
            print(f"  Subsection: {subsection['title']}")
            print(f"  Description: {subsection['description']}\n")