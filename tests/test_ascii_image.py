import unittest

from ascii_image import ArtImage


class TestArtImage(unittest.TestCase):
    """Test the ArtImage class."""

    def test_change_image_size(self):
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
        

if __name__ == "__main__":
    unittest.main()