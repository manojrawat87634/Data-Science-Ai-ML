import os
from PIL import Image

# Set your input and output folder paths
input_folder = 'images'
output_folder = os.path.join(input_folder, 'converted_webp')

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Supported extensions
supported_formats = ('.jpg', '.jpeg', '.png')

# Loop through files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(supported_formats):
        file_path = os.path.join(input_folder, filename)
        webp_filename = os.path.splitext(filename)[0] + '.webp'
        webp_path = os.path.join(output_folder, webp_filename)

        # Open and convert the image
        with Image.open(file_path) as img:
            img.save(webp_path, 'WEBP', quality=80)

