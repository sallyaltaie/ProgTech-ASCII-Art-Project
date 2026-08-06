import unittest

from session import Session 


class TestSession(unittest.TestCase):
    """Test the Session class."""

    def test_load_image(self):
        """Test loading an image."""
        session = Session()

        result = session.load_image("images/stadshuset.jpg")
        self.assertEqual(result, "Image loaded.")
        self.assertEqual(len(session.images), 1)

    def test_current_image(self):
        """Test that the loaded image becomes the current image."""
        session = Session()

        session.load_image("images/stadshuset.jpg")

        self.assertEqual(
            session.current_image.filename,
            "images/stadshuset.jpg"
        )

    def test_load_image_with_alias(self):
        """Test loading an image with an alias."""
        session = Session()

        session.load_image("images/stadshuset.jpg", "hus")
        image = session.get_image("hus")

        self.assertEqual(image.filename, "images/stadshuset.jpg")

    def test_set_image_setting(self):
        """Test changing an image setting."""
        session = Session()

        session.load_image("images/stadshuset.jpg")

        session.set_image_setting("current", "brightness", 1.5)

        self.assertEqual(session.current_image.brightness, 1.5)

    def test_save_session(self):
        """Test saving a session."""
        session = Session()

        session.load_image("images/stadshuset.jpg")

        result = session.save_session("tests/test_data/test_session.json")
        self.assertEqual(result, "Session saved.")

    def test_load_session(self):
        """Test loading a saved session."""
        session = Session()
        session.load_image("images/stadshuset.jpg")
        session.save_session("sessions/test_session.json")

        new_session = Session()
        result = new_session.load_session(
            "test/test_data/test_session.json"
        )

        self.assertEqual(result, "Session loaded.")

    def test_render(self):
        """Test rendering an image."""
        session = Session()
        session.load_image("images/stadshuset.jpg")

        ascii_art = session.render()

        self.assertEqual(type(ascii_art), str)
        self.assertNotEqual(ascii_art,"")

    def test_render_to_file(self):
        """Test that the rendered output file exists."""
        session = Session()
        session.load_image("images/stadshuset.jpg")

        result = session.render_to_file(
            "current",
            "tests/test_data/test_ascii.txt"
        )

        self.assertEqual(result, "ASCII art saved.")

        with open("tests/test_data/test_ascii.txt", "r") as file:
            content = file.read()
        self.assertNotEqual(content, "")

if __name__ == "__main__":
    unittest.main()