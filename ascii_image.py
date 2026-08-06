from PIL import Image


class ArtImage:
    """ Represents one image loaded into ASCII Art Studio """

    def __init__(self, filename, alias=None):
        """Initialize an ArtImage object."""
        self.filename = filename
        self.alias = alias

        with Image.open(filename) as img:
            # Save a copy of the image after the file is closed.
            self.image = img.copy() 

            # Save the original image size.
            self.original_width, self.original_height = img.size

        # Default render size.
        self.width = 50
        self.height = int(
            self.original_height * self.width / self.original_width
                          
        )

        # Default image settings
        self.brightness = 1.0
        self.contrast = 1.0

    # Setters
    def set_width(self, width):
        """Set the image's width and adjust height.""" 
        if width <= 0:
            raise ValueError("Width must be greater than zero.")
        
        self.width = width
        self.height = int(self.original_height * self.width / self.original_width
        )
        
    def set_height(self, height):
        """Set the image's height and adjust width."""
        if height <= 0:
            raise ValueError("Height must be greater than zero.")
        
        self.height = height
        self.width = int(self.original_width * self.height / self.original_height
        )

    def set_brightness(self, brightness):
        """Set the image brightness."""
        if brightness < 0:
            raise ValueError("Brightness cannot be negative.")

        self.brightness = brightness

    def set_contrast(self, contrast):
        """Set the image contrast"""
        if contrast < 0:
            raise ValueError("Contrast cannot be negative.")

        self.contrast = contrast

    def get_info(self):
        """Return information about the image"""
        return (
            f"filename: {self.filename}\n"
            f"size: ({self.original_width}, {self.original_height})\n"
            f"target size: ({self.width}, {self.height})\n"
            f"brightness:{self.brightness}\n"
            f"contrast: {self.contrast}"
        )