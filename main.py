
from session import Session

def main():
    """ Start the ASCII Art Studio! """
    # Test
    # image = ArtImage("images/stadshuset.jpg")
    # print(image.get_info())

    # ascii_art = render_image(image)
    # print(ascii_art)

    session = Session()
    session.load_image("images/stadshuset.jpg", "slalom")
    print(session.render())

    print(session.info())
    print()
    print(session.render())

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