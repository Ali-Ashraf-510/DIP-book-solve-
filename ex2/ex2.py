# 1. Import the Image module from PIL
from PIL import Image

# The path to the image
image_path = 'image.png'

try:
    # 2. Read the image
    img = Image.open(image_path)
    
    # 3. Show the image using your OS's default viewer
    img.show()
    
    # 4. Print details about the image to your terminal
    print(f"Image Format: {img.format}") # e.g., PNG, JPEG
    print(f"Image Mode: {img.mode}")   # e.g., RGB (color), L (grayscale)

except FileNotFoundError:
    print(f"Error: Could not find image at {image_path}")