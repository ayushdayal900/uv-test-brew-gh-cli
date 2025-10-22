import sys
from PIL import Image, ImageDraw, ImageFont

# Letters to use for ASCII art (lowercase letters only)
ASCII_CHARS = "abcdefghijklmnopqrstuvwxyz"

def resize_image(image, new_width=100):
    width, height = image.size
    # Keep aspect ratio; adjust height to compensate for character height
    aspect_ratio = height / float(width)
    new_height = max(1, int(aspect_ratio * new_width * 0.55))
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def map_pixels_to_chars(image, chars=ASCII_CHARS):
    pixels = image.getdata()
    # Map each pixel to a character from chars
    new_chars = [chars[pixel * (len(chars) - 1) // 255] for pixel in pixels]
    return ''.join(new_chars)

def image_to_ascii(image_path, new_width=100):
    image = Image.open(image_path)
    image = resize_image(image, new_width)
    image = grayify(image)
    ascii_str = map_pixels_to_chars(image, ASCII_CHARS)
    # Break into lines
    w = new_width
    ascii_lines = [ascii_str[index: index + w] for index in range(0, len(ascii_str), w)]
    return "\n".join(ascii_lines)

def ascii_to_image(ascii_art, font_path=None, font_size=12, bg_color="white", fg_color="black", output_path="mahadev_ascii.png"):
    lines = ascii_art.splitlines()
    if not lines:
        raise ValueError("ASCII art is empty")

    max_len = max(len(line) for line in lines)

    # Load a monospaced font if possible
    font = None
    if font_path:
        try:
            font = ImageFont.truetype(font_path, font_size)
        except Exception:
            font = None
    if font is None:
        font = ImageFont.load_default()

    # Rough size estimation
    char_width = font_size * 0.6
    char_height = font_size
    img_width = int(max_len * char_width)
    img_height = int(len(lines) * char_height * 1.1)

    img = Image.new("RGB", (img_width, img_height), color=bg_color)
    draw = ImageDraw.Draw(img)

    y = 0
    for line in lines:
        draw.text((0, y), line, fill=fg_color, font=font)
        y += char_height

    img.save(output_path)
    return output_path

def main():
    if len(sys.argv) < 2:
        print("Usage: python mahadev_ascii.py <image_path> [width] [output_image_path]")
        print("Example: python mahadev_ascii.py mahadev.jpg 120 mahadev_ascii.png")
        sys.exit(1)

    image_path = sys.argv[1]
    width = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    ascii_art = image_to_ascii(image_path, new_width=width)

    # Print ASCII art to console
    print(ascii_art)

    # Optional: save as an image of letters
    if len(sys.argv) > 3:
        out_path = sys.argv[3]
        ascii_to_image(ascii_art, output_path=out_path)
        print(f"Saved ASCII art as image: {out_path}")

if __name__ == "__main__":
    main()