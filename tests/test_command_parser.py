import unittest

from session import Session
from command_parser import CommandParser

TEST_IMAGE_1 = "images/stadshuset.jpg"
TEST_IMAGE_2 = "images/mickey.png"


class TestCommandParser(unittest.TestCase):
    """Test the CommandParser class."""

    def test_load_image_command(self):
        """Test the load image command."""
        session = Session()
        parser = CommandParser(session)

        result = parser.execute(
            "load image " + TEST_IMAGE_1
        )

        self.assertEqual(result, "Image loaded.")

    def test_load_image_with_alias_command(self):
        """Test loading an image with an alias."""
        session = Session()
        parser = CommandParser(session)

        parser.execute("load image " + TEST_IMAGE_2 + " as mickey")

        image = session.get_image("mickey")
        
        self.assertEqual(image.filename, TEST_IMAGE_2)

    def test_set_command(self):
        """Test the set command."""
        session = Session()
        parser = CommandParser(session)

        parser.execute("load image " + TEST_IMAGE_1)

        result = parser.execute("set current brightness 1.5")
        self.assertEqual(result, "Setting updated.")

    def test_unknown_command(self):
        """Test an unknown command."""
        session = Session()
        parser = CommandParser(session)

        result = parser.execute("hello")
        self.assertEqual(result, "Unknown command.")

    def test_quit_command(self):
        """Test the quit command."""
        session = Session()
        parser = CommandParser(session)

        result = parser.execute("quit")
        self.assertEqual(result, "quit")


if __name__ == "__main__":
    unittest.main()