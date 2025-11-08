# Cosmic Unicorn LED Matrix Pixel Plotter - Project Brief

## Project Overview
Build a web-based pixel plotting tool to design and plan LED matrix projects for the Cosmic Unicorn (32x32 LED matrix) connected to a Raspberry Pi Pico. This is both a practical tool and a learning project focused on understanding MicroPython and web development.

## Hardware Specs
- **Device**: Cosmic Unicorn 32x32 LED matrix
- **Controller**: Raspberry Pi Pico
- **Display**: 32x32 pixel grid (1,024 total pixels)
- **Control**: RGB color per pixel

## Technical Requirements

### Tool Architecture
- **Platform**: Web-based application
- **Deployment**: Docker Compose for local development
- **Future**: Potential public hosting capability
- **Environment**: Runs on development computer (not on Pico due to storage constraints)

### Core Features
1. **Interactive Pixel Grid**: 32x32 canvas where each pixel can be manually plotted
2. **RGB Color Picker**: Select any RGB color for each pixel
3. **Visual Preview**: Real-time visualization of the design
4. **Export Function**: Generate configuration file for upload to Pico
5. **Import Function** (nice to have): Load previously saved designs

### Export Format
- **Primary**: Text file with comma-separated values (e.g., `255,0,0,0,255,0,0,0,255,...`)
- **Flexibility**: Open to better formats as we discover them during development
- **Goal**: Easy to parse in MicroPython on the Pico

## Learning Objectives
This is an **educational project** with focus on:
- MicroPython fundamentals and best practices
- Web development with Python backend
- Docker containerization
- File I/O and data formatting
- RGB color manipulation
- Grid-based UI interaction

## Development Approach

### Explanation Requirements
For each step of the build, provide:
1. **Concept explanation**: What we're building and why
2. **Function documentation**: Clear explanation of each function's purpose
3. **MicroPython insights**: How this relates to MicroPython concepts
4. **Code walkthrough**: Line-by-line explanation for complex sections

### Interactive Coding Opportunities
**Mix of task sizes**:
- **Small guided tasks**: Individual functions with hints and starter code
- **Larger features**: Complete feature implementations with requirements and test cases
- **Mark clearly**: Indicate where I should code vs where you'll demonstrate

### Skill Level Context
- **Experience**: Beginner to intermediate Python
- **Background**: Some Python projects completed, nothing highly advanced
- **Learning goal**: Build practical skills while creating a useful tool

## Deliverables

### During Development
- Working web application with Docker Compose setup
- Pixel plotting interface (32x32 grid)
- RGB color selection tool
- Export functionality to text file
- Clear code comments and documentation
- Educational explanations at each stage

### End of Project
- **Final Summary** including:
  - What we built (feature overview)
  - Key MicroPython concepts learned
  - Function reference guide
  - How to use the tool
  - How to deploy the exported files to Pico
  - Next steps and potential enhancements

## Questions to Address During Build
- Optimal data format for Pico consumption
- Performance considerations for 1,024 pixels
- Best practices for MicroPython file handling
- Potential additional features (patterns, animations, etc.)

## Reference Materials
- Cosmic Unicorn: https://shop.pimoroni.com/products/space-unicorns?variant=40842626596947
- Pimoroni Unicorn GitHub: https://github.com/pimoroni/unicorn

---

**Ready to begin!** Start with project structure and Docker setup, explaining each decision and technology choice as we go.
