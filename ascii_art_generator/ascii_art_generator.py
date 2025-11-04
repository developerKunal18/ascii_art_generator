from PIL import Image

# ASCII characters used to represent pixel brightness
ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

def resize_image(image, new_width=100):
    """Resize the image maintaining the aspect ratio."""
    width, height = image.size
    ratio = height / width / 1.65  # Adjust ratio for text width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    """Convert image to grayscale."""
    return image.convert("L")

def pixels_to_ascii(image):
    """Map each pixel to an ASCII character."""
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return ascii_str

def convert_to_ascii(image_path, new_width=100):
    """Main function to convert an image into ASCII art."""
    try:
        image = Image.open(image_path)
    except:
        print("❌ Could not open image file.")
        return
    
    image = resize_image(image, new_width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)

    # Format the ASCII string into lines
    pixel_count = len(ascii_str)
    ascii_img = "\n".join([ascii_str[i:(i + new_width)] for i in range(0, pixel_count, new_width)])
    
    # Print result
    print(ascii_img)

    # Save output to a text file
    with open("ascii_art.txt", "w") as f:
        f.write(ascii_img)
    print("\n✅ ASCII art saved as 'ascii_art.txt'")

# Run program
image_path = input("🖼️ Enter image path: ")
convert_to_ascii(image_path)
