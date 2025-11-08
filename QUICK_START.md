# Quick Start Guide

## Run the Application

```bash
docker compose up --build
```

Open browser to: **http://localhost:5000**

## Use the Tool

1. **Pick a color** → Click color picker
2. **Paint pixels** → Click grid squares
3. **Export** → Click "Export Design" button
4. **Import** → Click "Import Design" button

## File Format

Exported as: `matrix_design_YYYYMMDD_HHMMSS.txt`

Format: `r1,g1,b1,r2,g2,b2,...` (3,072 values)

## Use on Raspberry Pi Pico

```python
# Load design
with open('design.txt', 'r') as f:
    pixels = [int(x) for x in f.read().split(',')]

# Display on Cosmic Unicorn
for i in range(1024):
    x = i % 32
    y = i // 32
    r, g, b = pixels[i*3], pixels[i*3+1], pixels[i*3+2]
    graphics.set_pen(graphics.create_pen(r, g, b))
    graphics.pixel(x, y)

cosmic.update(graphics)
```

## Coding Challenges

See `FINAL_SUMMARY.md` for 10 enhancement challenges!

### Quick Wins:
- Add "Fill All" button
- Add pixel counter
- Add random color button
- Add drawing mode (click & drag)

## Stop the Application

```bash
docker compose down
```

---

**Full documentation**: See `FINAL_SUMMARY.md`
**Project details**: See `PROJECT_BRIEF.md`
**Basic usage**: See `README.md`
