# alla bilder
# current
# save
# load

# Attribut 
# - images - blir dict
# - Current
import json

from ascii_image import ArtImage
from renderer import render_image

class Session:
    """Represents one ASCII Art Studio session."""

    # Constructor
    def __init__(self):
        """Initialize an empty session."""

        self.images = {} # dict
        self.current_image = None

    #Methods
    def load_image(self, filename, alias=None):
        """Load an image and make it the current image."""
        image = ArtImage(filename, alias)

        if alias is None:
            image_name = filename
        else:
            image_name = alias

        self.images[image_name] = image
        self.current_image = image

    def get_image(self, image_name):
        """Return an image by alias, filename or current."""

        if image_name == "current":
            return self.current_image

        if image_name in self.images:
            return self.images[image_name]

        # Search by original filename if no matching alias was found.
        for image in self.images.values():
            if image.filename == image_name:
                return image

        return None

    def info(self, image_name="current"):
        """Return information about an image."""
        image = self.get_image(image_name)

        if image is None:
            return "No image loaded"
        
        return image.get_info()

    def save_session(self, filename):
        """Save the current session to a JSON file."""

        session_data = {}
        images = {}

        for name in self.images:
            image = self.images[name]

            images[name] = {
                "filename": image.filename,
                "width": image.width,
                "height": image.height,
                "brightness": image.brightness, 
                "contrast": image.contrast

            }

        session_data["Images"] = images

        for name in self.current_image:
                session_data["current"] = name

        with open(filename, "w") as file:
            json.dump(session_data, file, indent=4)

    def load_session():
        pass
    def set_current():
        pass
    def remove_image():
        pass 

    def render(self):
        """Render current image"""

        image = self.get_image(image_name)

        if image is None:
            return "No image loaded."
        
        return render_image(self.current_image)