import os
import re

# Path to the images folder
folder_path = "images"

# Regex pattern to match photo_XXX.ext
pattern = re.compile(r"^photo_(\d{3})\.(webp|jpeg)$")

# First pass: rename to temporary names to avoid conflicts
temp_renames = []
final_renames = []
for filename in os.listdir(folder_path):
    match = pattern.match(filename)
    if match:
        number = int(match.group(1))
        ext = match.group(2)
        if number > 17:
            new_number = number - 1
            temp_filename = f"photo_{new_number:03d}_tmp.{ext}"
            final_filename = f"photo_{new_number:03d}.{ext}"
            old_path = os.path.join(folder_path, filename)
            temp_path = os.path.join(folder_path, temp_filename)
            final_path = os.path.join(folder_path, final_filename)
            temp_renames.append((old_path, temp_path))
            final_renames.append((temp_path, final_path))

# Rename to temporary files first
for old_path, temp_path in sorted(temp_renames, reverse=True):
    os.rename(old_path, temp_path)
    print(f"Temporarily renamed {old_path} -> {temp_path}")

# Then rename temporary files to final names
for temp_path, final_path in sorted(final_renames):
    os.rename(temp_path, final_path)
    print(f"Finalized rename {temp_path} -> {final_path}")