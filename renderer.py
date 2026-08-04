"""Functions for converting images into ASCII Art"""

from PIL import ImageEnhance 

ASCII_CHARACTERS = "@%#*+=-:. "

def adjust_brightness(image, brightness):
    """Adjust the image brightness"""
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(brightness)

def adjust_contrast(image, contrast):
    """Adjust the image contrast"""
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(contrast)

def resize_image(image, width, height):
    """Resize the image to the requested target size."""
    return image.resize((width, height)) # Tuple

def convert_to_grayscale(image):
    """Convert an image to grayscale"""
    return image.convert(mode="L") # "L" meaning -> 8-bit luminance

def pixels_to_ascii(image):
    """Convert grayscale pixels to ASCII characters."""

    pixels = image.getdata() # fetch all pixels
    ascii_string = "" # Create empty string

    for pixel in pixels: # Go through every pixel
        index = pixel * len(ASCII_CHARACTERS) // 256 # Calculate wich ASCII character should be used
        ascii_string +=  ASCII_CHARACTERS[index] # Add right ASCII character
        
    return ascii_string #result

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

    # ascii_string = pixels_to_ascii(image)
    ascii_rows = []

    for start in range(0, len(ascii_string), art_image.width):
        row = ascii_string[start:start + art_image.width]
        ascii_rows.append(row)

    return "\n".join(ascii_rows)