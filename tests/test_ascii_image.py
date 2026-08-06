import unittest

from ascii_image import ArtImage


class TestArtImage(unittest.TestCase):
    """Test the ArtImage class."""

    def test_default_settings(self):
        image = ArtImage("images/stadshuset.jpg")

        self.assertEqual(image.width, 50)
        self.assertEqual(image.brightness, 1.0)
        self.assertEqual(image.contrast, 1.0)

    def test_change_image_size(self):
        """Test changing the image width and height."""
        image = ArtImage("images/stadshuset.jpg")

        image.set_width(80)
        self.assertEqual(image.width, 80)

        expected_height = int(
            image.original_height * 80 / image.original_width
        )
        self.assertEqual(image.height, expected_height)

        image.set_height(40)
        self.assertEqual(image.height, 40)

        expected_width = int(
            image.original_width * 40 / image.original_height
        )
        self.assertEqual(image.width, expected_width)

    def test_change_image_settings(self):
        """Test changing brightness and contrast."""
        image = ArtImage("images/stadshuset.jpg")

        image.set_brightness(1.5)
        self.assertEqual(image.brightness, 1.5)

        image.set_contrast(0.8)
        self.assertEqual(image.contrast, 0.8)


if __name__ == "__main__":
    unittest.main()