import unittest

from ascii_image import ArtImage
from renderer import (
    adjust_brightness,
    adjust_contrast,
    resize_image,
    convert_to_grayscale,
    render_image
)


class TestRenderer(unittest.TestCase):
    """Test the renderer functions."""

    def test_resize_image(self):
        """Test resizing an image."""
        image = ArtImage("images/stadshuset.jpg")

        resized = resize_image(image.image, 80, 40)
        self.assertEqual(resized.size, (80, 40))

    def test_convert_to_grayscale(self):
        """Test converting an image to grayscale."""
        image = ArtImage("images/stadshuset.jpg")

        gray = convert_to_grayscale(image.image)
        self.assertEqual(gray.mode, "L")

    def test_adjust_brightness(self):
        """test adjusting image brightness"""
        image = ArtImage("images/stadshuset.jpg")

        brighter = adjust_brightness(image.image, 1.5)
        self.assertEqual(brighter.size, image.image.size)

    def test_render_image(self):
        """Test rendering an image to ASCII."""
        image = ArtImage("images/stadshuset.jpg")

        ascii_art = render_image(image)
        self.assertEqual(type(ascii_art), str)


if __name__ == "__main__":
    unittest.main()