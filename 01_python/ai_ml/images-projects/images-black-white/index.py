from PIL import Image

# Open the uploaded image
img_path = 'sop-logo-1-768x234-1.png'
img = Image.open(img_path).convert('RGBA')

# Process the image to change black to white
datas = img.getdata()
new_data = []
for item in datas:
    # Change black (and near-black) to white
    if item[0] < 50 and item[1] < 50 and item[2] < 50:
        new_data.append((255, 255, 255, item[3]))  # Preserve alpha channel
    else:
        new_data.append(item)

# Create new image with updated data
img.putdata(new_data)

# Save the new image
output_path = 'sop-logo-white.png'
img.save(output_path)
output_path