import os
import requests
from PIL import Image
from io import BytesIO

image_urls = [
    "https://lh3.googleusercontent.com/gps-cs-s/AC9h4nqj2dNhSa5fq9Wo18FZJDzCJWEJ22UifNieXoYqF9ViXrdunq5TI34z_PyD_i1xndNidgrLJ-XfWKNDgWkvaZ09GMY0PtrOhViYOM1ycfnUpVhlgx00MjPeybALHMp7ycnhxsU7=s680-w680-h510-rw",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSe05hl3FVh6K3wpaIy7419gbO773Otcq-rPg&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCBmebDzto9sKu5v9SYIaasgfeAkcL3Y0x0A&s",
    ]

output_folder = "webp_images"
os.makedirs(output_folder, exist_ok=True)

def download_and_convert_to_webp(url, index):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error if invalid response

        img = Image.open(BytesIO(response.content)).convert("RGB")  # To avoid alpha issue in JPEGs
        output_path = os.path.join(output_folder, f"image_{index + 1}.webp")
        img.save(output_path, format="WEBP", quality=85)

        print(f" Saved: {output_path}")
        return output_path
    except Exception as e:
        print(f" Failed to process {url}: {e}")
        return None

webp_paths = []

for i, url in enumerate(image_urls):
    path = download_and_convert_to_webp(url, i)
    if path:
        webp_paths.append(path)

import json
with open("converted_images.json", "w") as f:
    json.dump(webp_paths, f, indent=2)

print("\n All images processed.")
