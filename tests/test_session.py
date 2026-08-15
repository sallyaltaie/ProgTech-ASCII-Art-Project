import unittest

from session import Session 

TEST_IMAGE_1 = "images/stadshuset.jpg"
TEST_IMAGE_2 = "images/mickey.png"
# Files created by the tests and used only as test data.
TEST_SESSION_FILE = "tests/test_data/test_session.json"
TEST_ASCII_FILE = "tests/test_data/test_ascii.txt"

class TestSession(unittest.TestCase):
    """Test the Session class."""

    def test_load_image(self):
        """Test loading an image."""
        session = Session()

        result = session.load_image(TEST_IMAGE_1)
        self.assertEqual(result, "Image loaded.")
        self.assertEqual(len(session.images), 1)

    def test_current_image(self):
        """Test that the loaded image becomes the current image."""
        session = Session()

        session.load_image(TEST_IMAGE_1)

        self.assertEqual(
            session.current_image.filename,
            TEST_IMAGE_1
        )

    def test_load_image_with_alias(self):
        """Test loading an image with an alias."""
        session = Session()

        session.load_image(TEST_IMAGE_1, "hus")
        image = session.get_image("hus")

        self.assertEqual(image.filename, TEST_IMAGE_1)

    def test_set_image_setting(self):
        """Test changing an image setting."""
        session = Session()

        session.load_image(TEST_IMAGE_1)

        session.set_image_setting("current", "brightness", 1.5)

        self.assertEqual(session.current_image.brightness, 1.5)

    def test_save_session(self):
        """Test saving a session."""
        session = Session()

        session.load_image(TEST_IMAGE_1)

        result = session.save_session(TEST_SESSION_FILE)
        self.assertEqual(result, "Session saved.")

    def test_load_session(self):
        """Test loading a saved session."""
        session = Session()
        session.load_image(TEST_IMAGE_1)
        session.save_session(TEST_SESSION_FILE)

        new_session = Session()
        result = new_session.load_session(
            TEST_SESSION_FILE
        )

        self.assertEqual(result, "Session loaded.")

    def test_render(self):
        """Test rendering an image."""
        session = Session()
        session.load_image(TEST_IMAGE_1)

        ascii_art = session.render()

        self.assertEqual(type(ascii_art), str)
        self.assertNotEqual(ascii_art, "")

    def test_render_to_file(self):
        """Test that the rendered output file exists."""
        session = Session()
        session.load_image(TEST_IMAGE_1)

        result = session.render_to_file(
            "current",
            TEST_ASCII_FILE
        )

        self.assertEqual(result, "ASCII art saved.")

        with open(TEST_ASCII_FILE, "r") as file:
            content = file.read()
        self.assertNotEqual(content, "")

if __name__ == "__main__":
    unittest.main()