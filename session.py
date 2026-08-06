import json

from ascii_image import ArtImage
from renderer import render_image


class Session:
    """Represents one ASCII Art Studio session."""

    # Constructor
    def __init__(self):
        """Initialize an empty session."""

        self.images = {}
        self.current_image = None

    # Load / Save
    def load_image(self, filename, alias=None):
        """Load an image and make it the current image."""
        try:
            image = ArtImage(filename, alias)

        except OSError:
            return f"Could not open image file: {filename}"

        if alias is None:
            image_key = filename
        else:
            image_key = alias

        self.images[image_key] = image
        self.current_image = image

        return "Image loaded."

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

        try:
            with open(filename, "w") as file:
                json.dump(session_data, file, indent=4)

        except OSError:
            return f"Could not save session file: {filename}"

        return "Session saved."

    def load_session(self, filename):
        """Load a saved session from a JSON file."""
        try:
            with open(filename, "r") as file:
                session_data = json.load(file)
        except OSError:
            return f"Could not open session file: {filename}"
    
        except json.JSONDecodeError:
            return "The session file does not contain valid JSON."
    
        try:
            images_data = session_data["images"]
            current_key = session_data["current"]

        except (KeyError, TypeError):
            return "The session file has invalid data."
    
        self.images = {}
        self.current_image = None

        try:
            for image_key in images_data:
                image_data = images_data[image_key]
    
                result = self.load_image(image_data["filename"], image_data["alias"])
    
                if result != "Image loaded.":
                    return result
    
                # Restore the exact saved target size.
                image = self.get_image(image_key)
                image.width = image_data["width"]
                image.height = image_data["height"]
    
                image.set_brightness(image_data["brightness"])
                image.set_contrast(image_data["contrast"])

        except (KeyError, TypeError, ValueError):
            return "The session file has invalid data."
    
        if current_key is not None:
            self.current_image = self.get_image(current_key)
    
            if self.current_image is None:
                return "The session file has invalid data."
    
        else:
            self.current_image = None
    
        return "Session loaded."

    # Get information
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

    # Rendering
    def render(self, image_key="current"):
        """Render an image and make it the current image."""
        image = self.get_image(image_key)

        if image is None:
            return "No image loaded."

        self.current_image = image
        return render_image(image)

    def render_to_file(self, image_key, filename):
        """Render an image and save the ASCII art to a file."""
        image = self.get_image(image_key)
        
        if image is None:
            return "No image loaded."
        
        ascii_art = self.render(image_key)

        try:
            with open(filename, "w") as file:
                file.write(ascii_art)

        except OSError:
            return f"Could not write output file: {filename}"

        return "ASCII art saved."

    # Image settings 
    def set_image_setting(self, image_key, setting, value):
        """Set settings for an image."""
        image = self.get_image(image_key)

        if image is None:
            return "No image loaded."

        if setting == "width":
            image.set_width(value)

        elif setting == "height":
            image.set_height(value)

        elif setting == "brightness":
            image.set_brightness(value)

        elif setting == "contrast":
            image.set_contrast(value)

        else:
            return "Invalid setting."

        self.current_image = image
        return "Setting updated."