import os
from PIL import Image

# Configuration
INPUT_DIR = "in"
OUTPUT_DIR = "out"
DEFAULT_SIZE = 500  # target width/height in pixels
SUPPORTED_FORMATS = (".png", ".jpg", ".jpeg", ".webp", ".bmp")

def make_square(im, size=DEFAULT_SIZE, fill_color=(255, 255, 255, 0)):
    """Make the image square by padding with transparent background."""
    x, y = im.size
    new_size = max(size, x, y)
    new_im = Image.new("RGBA", (new_size, new_size), fill_color)
    new_im.paste(im, ((new_size - x) // 2, (new_size - y) // 2), im)
    return new_im

def resize_image(im, size=DEFAULT_SIZE):
    """Resize image keeping aspect ratio."""
    im.thumbnail((size, size), Image.Resampling.LANCZOS)
    return im

def process_images():
    """Convert all images in INPUT_DIR and save resized PNGs with transparency to OUTPUT_DIR."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(SUPPORTED_FORMATS):
            infile = os.path.join(INPUT_DIR, filename)
            base, _ = os.path.splitext(filename)
            outfile = os.path.join(OUTPUT_DIR, base + ".png")  # always save as .png

            try:
                with Image.open(infile) as im:
                    im = im.convert("RGBA")  # ensure transparency support
                    im_resized = resize_image(im, DEFAULT_SIZE)
                    im_square = make_square(im_resized, DEFAULT_SIZE)
                    im_square.save(outfile, format="PNG")
                    print(f"Converted: {filename} → {outfile}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

if __name__ == "__main__":
    process_images()
    print("All images processed.")
