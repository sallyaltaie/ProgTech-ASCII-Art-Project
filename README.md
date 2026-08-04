                User
                  │
                  ▼
          CommandParser
                  │
                  ▼
              Session
           ┌───────────┐
           │           │
           ▼           ▼
     ASCIIImage   ASCIIImage
           │
           ▼
        Renderer

ASCII-Art-Studio/
│
├── main.py
├── art_image.py        ← Klassen ArtImage
├── session.py          ← Klassen Session
├── command_parser.py   ← Tolkar kommandon
├── renderer.py         ← ALL rendering
│
├── images/
├── output/
├── sessions/
└── tests/