# QR Code Generator

This is a simple Python project to generate QR codes for any website link you provide. The generated QR code is saved as an image file and displayed automatically.

## Features

- Generates a QR code from a user-provided website URL
- Saves the QR code as `output_qr.png`
- Displays the QR code image after creation

## Requirements

- Python 3.x
- [qrcode](https://pypi.org/project/qrcode/) Python library

## Installation

1. Clone or download this repository.
2. Install the required package:
 ```powershell
 pip install qrcode pillow
 ```

## Usage

Run the script using Python:

```powershell
python main.py
```

You will be prompted to enter a website URL. The script will generate a QR code and save it as `output_qr.png` in the project directory, then display the image.

## Example

```
Please give me your website: https://www.example.com
```

The file `output_qr.png` will be created with the QR code for the provided link.


