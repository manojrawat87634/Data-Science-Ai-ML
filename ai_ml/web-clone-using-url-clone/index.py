import os
import requests
from urllib.parse import urljoin, urlparse
from playwright.sync_api import sync_playwright

# CHANGE THIS to the site you want to clone
SITE_URL = input("Enter the url ")
OUTPUT_DIR = "cloned_site"

def save_file_from_url(resource_url, base_folder):
    try:
        parsed_url = urlparse(resource_url)
        path = parsed_url.path
        if path.endswith("/"):
            path += "index.html"
        file_path = os.path.join(base_folder, path.lstrip("/"))

        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        response = requests.get(resource_url, timeout=10)
        if response.ok:
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"[+] Saved: {path}")
        else:
            print(f"[!] Failed to download {resource_url}")
    except Exception as e:
        print(f"[!] Error downloading {resource_url}: {e}")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        print(f"[+] Opening {SITE_URL}")
        page.goto(SITE_URL, wait_until="networkidle", timeout=60000)  # 60 seconds

        # Save full page HTML
        html_content = page.content()
        with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_content)
        print("[+] HTML saved")

        # Extract resources: images, CSS, JS
        resource_urls = page.eval_on_selector_all(
            "img[src], script[src], link[rel=stylesheet][href]",
            "elements => elements.map(el => el.src || el.href)"
        )

        for url in set(resource_urls):
            if url.startswith("data:"):
                continue  # skip base64
            absolute_url = urljoin(SITE_URL, url)
            save_file_from_url(absolute_url, OUTPUT_DIR)

        browser.close()
        print(f"Cloning completed to '{OUTPUT_DIR}'")

if __name__ == "__main__":
    main()
