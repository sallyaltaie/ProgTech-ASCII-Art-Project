# ASCII Art Studio

ASCII Art Studio is a command line application written in Python that converts images into ASCII art.
Users can load images, adjust rendering settings, manage multiple images in a session, and save both ASCII output and session data.

The project was developed as part of a programming course and implements an object-oriented solution for managing multiple images, rendering them as ASCII art, and saving or restoring work sessions.

## Features

- Load JPG and PNG images
- Convert images to ASCII art
- Manage multiple images in one session
- Use filenames or aliases to identify images
- Adjust:
  - Width
  - Height
  - Brightness
  - Contrast
- Save rendered ASCII art to a text file
- Save and load sessions using JSON
- Command-line interface
- Unit tests using Python's `unittest` framework

## Project Structure

```
ASCII-Art-Studio/
├── ascii_image.py
├── renderer.py
├── session.py
├── command_parser.py
├── main.py
├── images/
├── output/
├── sessions/
├── tests/
└── requirements.txt
```
## Architecture

The application is divided into separate modules with clear responsibilities:

- **ArtImage** – stores image data and rendering settings.
- **Renderer** – converts images into ASCII art.
- **Session** – manages loaded images and saved sessions.
- **CommandParser** – parses and executes user commands.
- **main.py** – starts the application and handles user interaction.

## Requirements

- Python 3.13.7
- Pillow 12.3.0

Install the required package:

```bash
pip install -r requirements.txt
```

## Running the Program

Start the application:

```bash
python main.py
```

## Running the Tests

Run all unit tests:

```bash
python -m unittest discover -s tests
```

## Supported Commands

| Command | Description |
|---------|-------------|
| `load image <file>` | Load an image |
| `load image <file> as <alias>` | Load an image with an alias |
| `load session <file>` | Load a saved session |
| `info` | Display information about loaded images |
| `render` | Render the current image |
| `render <image>` | Render a specific image |
| `render <image> to <file>` | Save rendered ASCII art to a text file |
| `set <image> width <value>` | Change image width |
| `set <image> height <value>` | Change image height |
| `set <image> brightness <value>` | Adjust brightness |
| `set <image> contrast <value>` | Adjust contrast |
| `save session as <file>` | Save the current session |
| `quit` | Exit the application |

## Testing

The project includes unit tests for:

- ArtImage
- Renderer
- Session
- CommandParser

Run all tests using:

```bash
python -m unittest discover -s tests
```

## Author 

Sally Altaie 