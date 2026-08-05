import json

from ascii_image import ArtImage
from renderer import render_image

class Session:
    """Represents one ASCII Art Studio session."""

    # Constructor
    def __init__(self):
        """Initialize an empty session."""

        self.images = {} # dictionary containing all loaded images.
        self.current_image = None

    # Methods
    def load_image(self, filename, alias=None):
        """Load an image and make it the current image."""
        image = ArtImage(filename, alias)

        if alias is None:
            image_key = filename
        else:
            image_key = alias

        self.images[image_key] = image
        self.current_image = image

    def get_image(self, image_key):
        """Return an image by alias, filename or current."""

        if image_key == "current":
            return self.current_image

        if image_key in self.images:
            return self.images[image_key]

        # Search by original filename if no matching alias was found.
        for image in self.images.values():
            if image.filename == image_key:
                return image

        return None

    def info(self):
        """Return information about all images in the session."""
        if len(self.images) == 0:
            return "No image loaded."

        information = "=== Current Session ===\n"
        information += "Images:\n"

        current_key = None

        for image_key in self.images:
            image = self.images[image_key]

            information += image_key + "\n"
            information += image.get_info() + "\n"

            if image is self.current_image:
                current_key = image_key

        information += "Current image: " + str(current_key)

        return information
        
    
    def save_session(self, filename):
        """Save the current session to a JSON file."""

        session_data = {}
        images_data = {}
        current_key = None

        for image_key in self.images:
            image = self.images[image_key]

            image_data = {
                "filename": image.filename,
                "alias": image.alias,
                "width": image.width,
                "height": image.height,
                "brightness": image.brightness, 
                "contrast": image.contrast

            }

            images_data[image_key] = image_data

            if image is self.current_image:
                current_key = image_key

        session_data["images"] = images_data
        session_data["current"] = current_key

        with open(filename, "w") as file:
            json.dump(session_data, file, indent=4)

    def load_session(self, filename):
        """Load a saved session from a JSON file."""

        with open(filename, "r") as file:
            session_data = json.load(file)

        self.images = {}
        self.current_image = None

        for image_key in session_data["images"]:
            image_data = session_data["images"][image_key]

            self.load_image(image_data["filename"], image_data["alias"])

            image = self.get_image(image_key)
            image.width = image_data["width"]
            image.height = image_data["height"]
            
            image.set_brightness = image_data["brightness"]
            image.set_contrast = image_data["contrast"]

        self.current_image = self.get_image(session_data["current"])

    def render(self, image_key="current"):
        """Render an image and make it the current image."""

        image = self.get_image(image_key)

        if image is None:
            return "No image loaded."

        self.current_image = image
        
        return render_image(image)