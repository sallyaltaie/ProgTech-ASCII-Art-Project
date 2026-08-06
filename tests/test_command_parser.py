import unittest

from session import Session
from command_parser import CommandParser


class TestCommandParser(unittest.TestCase):
    """The the CommandParser class."""

    def test_load_image_command(self):
        """Test the load iamge command"""
        session = Session()
        parser = CommandParser(session)

        result = parser.execute(
            "load image images/stadshuset.jpg"
        )

        self.assertEqual(result, "Image loaded.")

    def test_load_image_with_alias_command(self):
        """The loading an image with an alias."""
        session = Session()
        parser = CommandParser(session)

        parser.execute("load image images/stadshuset.jpg as hus")

        image = session.get_image("hus")
        
        image = self.assertEqual(image.filename, "images/stadshuset.jpg")

    def test_set_command(self):
        """Test the set command."""
        session = Session()
        parser = CommandParser(session)

        parser.execute("load image images/stadshuset.jpg")

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