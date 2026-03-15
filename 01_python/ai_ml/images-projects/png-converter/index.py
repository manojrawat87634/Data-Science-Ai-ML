from rembg import remove
from PIL import Image, ImageEnhance
import os

def enhance_image(img):
    # Resize to 2x for better edge detection
    img = img.resize((img.width * 2, img.height * 2), Image.LANCZOS)

    # Increase sharpness
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(2.0)

    # Increase contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1.5)

    return img

def remove_background(input_path, output_path):
    # Open and enhance image
    img = Image.open(input_path).convert("RGBA")
    enhanced_img = enhance_image(img)

    # Save to bytes
    from io import BytesIO
    buffer = BytesIO()
    enhanced_img.save(buffer, format="PNG")
    input_data = buffer.getvalue()

    # Remove background
    output_data = remove(input_data)

    # Save result
    with open(output_path, 'wb') as out_file:
        out_file.write(output_data)
    print(f"✅ Background removed and saved to: {output_path}")

# Example usage
input_image = "lg.jpeg"  # your image file
output_image = os.path.splitext(input_image)[0] + "_no_bg.png"

remove_background(input_image, output_image)
