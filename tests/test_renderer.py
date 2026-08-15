import unittest

from ascii_image import ArtImage

TEST_IMAGE_1 = "images/stadshuset.jpg"
TEST_IMAGE_2 = "images/mickey.png"

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
        image = ArtImage(TEST_IMAGE_1)

        resized = resize_image(image.image, 80, 40)
        self.assertEqual(resized.size, (80, 40))

    def test_convert_to_grayscale(self):
        """Test converting an image to grayscale."""
        image = ArtImage(TEST_IMAGE_2)

        gray = convert_to_grayscale(image.image)
        self.assertEqual(gray.mode, "L")

    def test_adjust_brightness(self):
        """Test adjusting image brightness."""
        image = ArtImage(TEST_IMAGE_1)

        brighter = adjust_brightness(image.image, 1.5)
        self.assertEqual(brighter.size, image.image.size)

    def test_adjust_contrast(self):
        """Test adjusting image contrast."""
        image = ArtImage(TEST_IMAGE_1)

        contrast = adjust_contrast(image.image, 0.8)
        self.assertEqual(contrast.size, image.image.size)
        
    def test_render_image(self):
        """Test rendering an image to ASCII."""
        image = ArtImage(TEST_IMAGE_1)

        ascii_art = render_image(image)
        self.assertEqual(type(ascii_art), str)


if __name__ == "__main__":
    unittest.main()