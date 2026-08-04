
from ascii_image import ArtImage
from renderer import render_image

def main():
    """ Start the ASCII Art Studio! """
    image = ArtImage("images/stadshuset.jpg")

    print(image.get_info())

    ascii_art = render_image(image)
    print(ascii_art)

if __name__ == "__main__":
    main()

# Start
# ↓
# Skapa Session
# ↓
# Skapa Parser
# ↓
# Loop
# ↓
# Läs kommando
# ↓
# Parser kör rätt metod