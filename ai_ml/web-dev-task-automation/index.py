import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
from urllib.parse import urljoin

def get_html_content():
    choice = input("Choose input type:\n1. Web URL\n2. Local HTML file\nEnter 1 or 2: ").strip()
    if choice == "1":
        url = input("Enter webpage URL: ").strip()
        response = requests.get(url)
        return response.text, url
    elif choice == "2":
        file_path = input("Enter path to local HTML file: ").strip()
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read(), "file:///" + os.path.abspath(file_path)
    else:
        print("Invalid choice.")
        exit(1)

def extract_image_urls(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    img_urls = []
    for img in soup.find_all("img"):
        src = img.get("src") or img.get("data-src")
        if src:
            full_url = urljoin(base_url, src)
            img_urls.append(full_url)
    print(f"Found {len(img_urls)} image(s).")
    return img_urls

def download_and_convert_to_webp(img_urls, output_dir="webp_images"):
    os.makedirs(output_dir, exist_ok=True)

    for idx, img_url in enumerate(img_urls):
        try:
            print(f"Downloading {img_url}")
            response = requests.get(img_url, timeout=10)
            image = Image.open(BytesIO(response.content)).convert("RGB")
            filename = f"image_{idx+1}.webp"
            image.save(os.path.join(output_dir, filename), "WEBP")
            print(f"Saved: {filename}")
        except Exception as e:
            print(f"Error with {img_url}: {e}")

def main():
    html, base_url = get_html_content()
    img_urls = extract_image_urls(html, base_url)
    download_and_convert_to_webp(img_urls)

if __name__ == "__main__":
    main()
