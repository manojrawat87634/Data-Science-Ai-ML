import re
import json
import requests
from bs4 import BeautifulSoup

def extract_background_images(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    bg_images = []

    # Extract from inline styles
    for tag in soup.find_all(style=True):
        style = tag['style']
        matches = re.findall(r'background(?:-image)?:\s*url\(([^)]+)\)', style, re.IGNORECASE)
        bg_images.extend([url.strip('\'"') for url in matches])

    # Extract from <style> blocks
    for style_tag in soup.find_all('style'):
        css = style_tag.string
        if css:
            matches = re.findall(r'background(?:-image)?:\s*url\(([^)]+)\)', css, re.IGNORECASE)
            bg_images.extend([url.strip('\'"') for url in matches])

    return list(set(bg_images))  # Optional: remove duplicates

def main():
    print("Choose input method:")
    print("1. Enter URL")
    print("2. Enter local HTML file path")

    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == '1':
        url = input("Enter full webpage URL: ").strip()
        try:
            response = requests.get(url)
            response.raise_for_status()
            html_content = response.text
        except Exception as e:
            print(f"Failed to fetch URL: {e}")
            return

    elif choice == '2':
        file_path = input("Enter local HTML file path: ").strip()
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
        except FileNotFoundError:
            print("File not found.")
            return
    else:
        print("Invalid choice.")
        return

    bg_images = extract_background_images(html_content)
    result = {
        "image_url": bg_images
    }

    print(f"\n Found {len(bg_images)} background image URL(s):")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
