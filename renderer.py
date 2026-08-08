"""Functions for converting images into ASCII art."""

from PIL import ImageEnhance 


# Fixed scale from dark to light used for all ASCII rendering.
ASCII_CHARACTERS = "@%#*+=-:. "


def adjust_brightness(image, brightness):
    """Adjust the image brightness."""
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(brightness)

def adjust_contrast(image, contrast):
    """Adjust the image contrast."""
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(contrast)

def resize_image(image, width, height):
    """Resize the image to the requested target size."""
    return image.resize((width, height))

def convert_to_grayscale(image):
    """Convert an image to 8-bit grayscale."""
    return image.convert(mode="L") 

def pixels_to_ascii(image):
    """Convert grayscale pixels to ASCII characters."""
    pixels = image.getdata()
    ascii_string = "" 

    for pixel in pixels: 
        index = pixel * len(ASCII_CHARACTERS) // 256
        ascii_string += ASCII_CHARACTERS[index]
        
    return ascii_string 

def render_image(art_image):
    """Render an ArtImage object as ASCII art."""
    image = art_image.image.copy()

    image = adjust_brightness(image, art_image.brightness)
    image = adjust_contrast(image, art_image.contrast)
    image = resize_image(
        image, 
        art_image.width, 
        art_image.height
    )
    image = convert_to_grayscale(image)

    ascii_string = pixels_to_ascii(image)
    ascii_rows = []

    for start in range(0, len(ascii_string), art_image.width):
        row = ascii_string[start:start + art_image.width]
        ascii_rows.append(row)

    return "\n".join(ascii_rows)