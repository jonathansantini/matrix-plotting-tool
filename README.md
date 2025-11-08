# Cosmic Unicorn Matrix Plotter

A web-based tool for designing pixel art for the Cosmic Unicorn 32x32 LED matrix.

## Quick Start

```bash
# Start the application
docker compose up --build

# Access the app
# Open browser to: http://localhost:5001
```

## Features

- 32x32 interactive pixel grid
- RGB color picker
- Export designs to text files
- Import previously saved designs
- One-click grid clearing

## Export Format

Exported files contain comma-separated RGB values:
```
255,0,0,0,255,0,0,0,255,...
```

Format: `r1,g1,b1,r2,g2,b2,...` (3,072 values total)

## Using Exported Files on Raspberry Pi Pico

### Basic MicroPython Example:

```python
# Load your exported design
def load_design(filename):
    with open(filename, 'r') as f:
        data = f.read()
        values = [int(x) for x in data.split(',')]
    return values

# Use with Cosmic Unicorn
from picounicorn import PicoUnicorn
unicorn = PicoUnicorn()

pixels = load_design('matrix_design_20240101_120000.txt')

# Display each pixel
for i in range(1024):
    x = i % 32
    y = i // 32
    r = pixels[i * 3]
    g = pixels[i * 3 + 1]
    b = pixels[i * 3 + 2]
    unicorn.set_pixel(x, y, r, g, b)
```

## Project Structure

```
matrix-plotting-tool/
├── app/
│   ├── main.py              # Flask backend
│   ├── templates/
│   │   └── index.html       # Frontend UI
│   └── static/              # (future CSS/JS files)
├── exports/                 # Saved designs
├── docker-compose.yml       # Docker orchestration
├── Dockerfile              # Container definition
└── requirements.txt        # Python dependencies
```

## Development

Files are mounted as volumes - changes to code are reflected immediately without rebuild!

## Stopping the Application

```bash
# Stop containers
docker compose down
```
