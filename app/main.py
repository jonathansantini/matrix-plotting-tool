"""
Cosmic Unicorn Matrix Plotter - Main Flask Application

This web server handles:
1. Serving the pixel plotting interface (HTML/CSS/JS)
2. Saving pixel designs to files
3. Loading previously saved designs
"""

from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
import os
import json
from datetime import datetime

# Initialize Flask application
# __name__ helps Flask know where to find templates and static files
app = Flask(__name__)

# Enable CORS (Cross-Origin Resource Sharing)
# Allows frontend JavaScript to make requests to this backend
CORS(app)

# Directory where we'll save exported designs
EXPORTS_DIR = '/app/exports'

# Ensure exports directory exists
os.makedirs(EXPORTS_DIR, exist_ok=True)


@app.route('/')
def index():
    """
    Main page route - serves the pixel plotter interface

    When user visits http://localhost:5000, this function runs
    and returns the HTML template
    """
    return render_template('index.html')


@app.route('/api/export', methods=['POST'])
def export_design():
    """
    Export pixel data to a text file

    Expects JSON data with 'pixels' array containing RGB values
    Format: [r1, g1, b1, r2, g2, b2, ...]

    Returns: JSON with filename and download URL
    """
    try:
        # Get JSON data from request body
        data = request.get_json()

        # Extract pixel array
        pixels = data.get('pixels', [])

        # Validate we have correct number of values (32x32 pixels * 3 RGB values)
        expected_values = 32 * 32 * 3
        if len(pixels) != expected_values:
            return jsonify({
                'error': f'Expected {expected_values} values, got {len(pixels)}'
            }), 400

        # Generate filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'matrix_design_{timestamp}.txt'
        filepath = os.path.join(EXPORTS_DIR, filename)

        # Convert pixel array to comma-separated string
        pixel_string = ','.join(map(str, pixels))

        # Write to file
        with open(filepath, 'w') as f:
            f.write(pixel_string)

        return jsonify({
            'success': True,
            'filename': filename,
            'message': f'Design exported successfully!'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/import', methods=['POST'])
def import_design():
    """
    Import pixel data from uploaded file

    Expects: File upload with comma-separated RGB values
    Returns: JSON with pixel array
    """
    try:
        # Check if file was uploaded
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        # Read file content
        content = file.read().decode('utf-8')

        # Parse comma-separated values
        pixels = [int(x.strip()) for x in content.split(',')]

        # Validate length
        expected_values = 32 * 32 * 3
        if len(pixels) != expected_values:
            return jsonify({
                'error': f'Invalid file format. Expected {expected_values} values, got {len(pixels)}'
            }), 400

        return jsonify({
            'success': True,
            'pixels': pixels
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/download/<filename>')
def download_file(filename):
    """
    Download exported design file

    Args:
        filename: Name of file to download from exports directory
    """
    try:
        filepath = os.path.join(EXPORTS_DIR, filename)

        if not os.path.exists(filepath):
            return jsonify({'error': 'File not found'}), 404

        return send_file(filepath, as_attachment=True)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Run Flask development server
# Only runs when you execute this file directly (not with gunicorn)
if __name__ == '__main__':
    # host='0.0.0.0' allows access from outside container
    # debug=True enables auto-reload and better error messages
    app.run(host='0.0.0.0', port=5000, debug=True)
