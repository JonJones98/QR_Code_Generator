# QR Code Generator

A web-based QR code generator built with Flask that allows users to create QR codes from URLs and download them in various image formats.

## Features

- **URL to QR Code Conversion**: Generate QR codes from any valid URL
- **Multiple Image Formats**: Support for various image formats including:
  - `.png` (default)
  - `.jpg/.jpeg`
  - `.gif`
  - `.bmp`
  - `.tif/.tiff`
  - `.eps`
  - `.pdf`
  - And more
- **Custom Filenames**: Users can specify custom names for their QR code files
- **Download Functionality**: Direct download of generated QR codes
- **Form Validation**: Input validation to ensure all required fields are provided
- **Clean Interface**: Simple and intuitive web interface

## Tech Stack

- **Backend**: Flask (Python)
- **QR Code Generation**: Python `qrcode` library
- **Frontend**: HTML templates with CSS styling
- **Database**: MySQL (configured but not actively used in current implementation)
- **Containerization**: Docker support

## Project Structure

```
QR_Code_Generator/
├── flask_app/
│   ├── __init__.py              # Flask app initialization
│   ├── controllers/
│   │   └── qrcode.py           # Main application routes and logic
│   ├── models/
│   │   └── qrcode.py           # Data validation logic
│   ├── config/
│   │   └── mysqlconnection.py  # Database connection configuration
│   ├── static/
│   │   ├── image_folder/       # Generated QR code storage
│   │   └── styles/
│   │       └── style.css       # Application styling
│   └── templates/              # HTML templates
│       ├── dashboard.html
│       ├── home_page.html
│       ├── index.html
│       ├── download_page.html
│       ├── succesfulQRCreation.html
│       └── errorQRCreation.html
├── server.py                   # Application entry point
├── wsgi.py                     # WSGI configuration
├── requirements.txt            # Python dependencies
├── Pipfile                     # Pipenv configuration
├── Dockerfile                  # Docker configuration
└── README.md                   # This file
```

## Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

### Option 1: Standard Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/JonJones98/QR_Code_Generator.git
   cd QR_Code_Generator
   ```

2. **Install dependencies**:
   ```bash
   pip install flask qrcode[pil]
   ```

3. **Run the application**:
   ```bash
   python server.py
   ```

### Option 2: Using Pipenv

1. **Clone the repository**:
   ```bash
   git clone https://github.com/JonJones98/QR_Code_Generator.git
   cd QR_Code_Generator
   ```

2. **Install Pipenv** (if not already installed):
   ```bash
   pip install pipenv
   ```

3. **Install dependencies and activate virtual environment**:
   ```bash
   pipenv install flask qrcode[pil]
   pipenv shell
   ```

4. **Run the application**:
   ```bash
   python server.py
   ```

### Option 3: Using Docker

1. **Clone the repository**:
   ```bash
   git clone https://github.com/JonJones98/QR_Code_Generator.git
   cd QR_Code_Generator
   ```

2. **Build and run with Docker**:
   ```bash
   docker build -t qr-generator .
   docker run -p 5000:5000 qr-generator
   ```

## Usage

1. **Start the application** using one of the installation methods above
2. **Open your web browser** and navigate to `http://localhost:5000`
3. **Enter a URL** that you want to convert to a QR code
4. **Specify a filename** for your QR code image
5. **Select the desired image format** from the dropdown menu
6. **Click "Generate"** to create your QR code
7. **Download** your QR code image

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main dashboard/landing page |
| `/qr/create` | GET | QR code creation form |
| `/qr/constructing` | POST | Process QR code creation request |
| `/qr/complete` | GET | Generate and save QR code |
| `/qr/download` | GET | Download page for generated QR code |
| `/qr/reset` | GET | Clear session and clean up files |

## Configuration

The application uses Flask sessions to maintain state between requests. The secret key is configured in `flask_app/__init__.py`:

```python
app.secret_key = "*****"  # Change this in production!
```

**⚠️ Important**: Change the secret key to a secure random value in production environments.

## File Management

- Generated QR codes are temporarily stored in `flask_app/static/image_folder/`
- The application automatically cleans up old files when creating new QR codes
- Files are removed when the session is reset

## Development

### Running in Debug Mode

The application runs in debug mode by default when started with `python server.py`. This enables:
- Automatic code reloading
- Detailed error messages
- Debug toolbar

### Adding New Features

1. **Routes**: Add new routes in `flask_app/controllers/qrcode.py`
2. **Templates**: Create new HTML templates in `flask_app/templates/`
3. **Styling**: Modify CSS in `flask_app/static/styles/style.css`
4. **Validation**: Add validation logic in `flask_app/models/qrcode.py`

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source. Please check the repository for license details.

## Troubleshooting

### Common Issues

1. **"Module not found" errors**: Ensure all dependencies are installed
   ```bash
   pip install flask qrcode[pil]
   ```

2. **Permission errors**: Make sure the application has write permissions for the `image_folder` directory

3. **Port already in use**: If port 5000 is busy, modify `server.py` to use a different port:
   ```python
   app.run(debug=True, port=5001)
   ```

### Dependencies

The main dependencies for this project are:
- `flask`: Web framework
- `qrcode[pil]`: QR code generation with PIL support

## Author

**Jon Jones** - [JonJones98](https://github.com/JonJones98)

## Acknowledgments

- Built with the Python `qrcode` library
- Powered by Flask web framework
