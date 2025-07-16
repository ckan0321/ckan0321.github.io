import os
from PIL import Image

# Define the path to the images directory
images_dir = os.path.join(os.path.dirname(__file__), 'images')

# Specify the target filename
original_filename = "photo_057.jpeg"
original_path = os.path.join(images_dir, original_filename)

# No renaming needed; proceed to convert to .webp
with Image.open(original_path) as img:
    webp_filename = "photo_057.webp"
    webp_path = os.path.join(images_dir, webp_filename)
    img.save(webp_path, "WEBP")
    print(f"Created: {webp_filename}")