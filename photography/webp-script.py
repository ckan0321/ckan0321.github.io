import os

# Directory containing your images (adjust if needed)
IMAGE_DIR = "photography/images"

# Output HTML file
OUTPUT_FILE = "gallery.html"

# Get sorted list of base filenames that have both .webp and .jpg
files = os.listdir(IMAGE_DIR)
base_names = sorted(set(
    os.path.splitext(f)[0]
    for f in files
    if f.endswith(".webp") and f.replace(".webp", ".jpg") in files
))

# Generate HTML
html = []
html.append('<main class="gallery">')

for name in base_names:
    webp_path = f"{IMAGE_DIR}/{name}.webp"
    jpg_path = f"{IMAGE_DIR}/{name}.jpg"
    html.append(f'  <a href="{jpg_path}" download>')
    html.append(f'    <img src="{webp_path}" alt="Photo {name}" loading="lazy" />')
    html.append('  </a>')

html.append('</main>')

# Write to file
with open(OUTPUT_FILE, "w") as f:
    f.write("\n".join(html))

print(f"Generated gallery HTML in {OUTPUT_FILE}")