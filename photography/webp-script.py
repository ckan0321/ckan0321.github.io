

import os
import re
from PIL import Image

# Define the path to the images directory
images_dir = os.path.join(os.path.dirname(__file__), 'images')

# Regex pattern to match "photo - ###.jpeg"
pattern = re.compile(r'^photo - (\d{1,3})\.jpeg$', re.IGNORECASE)

for filename in os.listdir(images_dir):
    match = pattern.match(filename)
    if match:
        number = match.group(1).zfill(3)  # Pad with zeros to make it 3 digits
        old_path = os.path.join(images_dir, filename)
        new_filename = f"photo_{number}.jpeg"
        new_path = os.path.join(images_dir, new_filename)

        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")

        # Convert to .webp
        with Image.open(new_path) as img:
            webp_filename = f"photo_{number}.webp"
            webp_path = os.path.join(images_dir, webp_filename)
            img.save(webp_path, "WEBP")
            print(f"Created: {webp_filename}")