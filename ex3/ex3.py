import cv2
from PIL import Image
import numpy as np # OpenCV images are numpy arrays

# The path to the image we are testing
image_path = 'image.png'

print("--- 1. Testing with OpenCV ---")

# --- OpenCV Color ---
# Load as a color image (flag = 1)
img_color = cv2.imread(image_path, 1) 

if img_color is not None:
    print("\n[OpenCV - Color Image]")
    print(f"Type of object: {type(img_color)}")
    # Note the order: (height, width, channels)
    print(f"Shape (h, w, c): {img_color.shape}") 
    
    # Unpack the shape tuple
    h, w, c = img_color.shape
    print(f"  Height (h): {h} pixels")
    print(f"  Width (w):  {w} pixels")
    print(f"  Channels (c): {c}")
    
    # Other properties from your lesson
    print(f"Data Type (dtype): {img_color.dtype}")
    print(f"Total elements (h*w*c): {img_color.size}") 
    print(f"Min pixel value: {img_color.min()}")
    print(f"Max pixel value: {img_color.max()}")
else:
    print(f"Error: OpenCV could not load color image at {image_path}")

# --- OpenCV Grayscale ---
# Load as a grayscale image (flag = 0)
img_gray = cv2.imread(image_path, 0) 

if img_gray is not None:
    print("\n[OpenCV - Grayscale Image]")
    # Note the order: (height, width)
    print(f"Shape (h, w): {img_gray.shape}") 
    
    # Unpack the shape tuple
    h_g, w_g = img_gray.shape
    print(f"  Height (h): {h_g} pixels")
    print(f"  Width (w):  {w_g} pixels")
    print(f"Total elements (h*w): {img_gray.size}")
else:
    print(f"Error: OpenCV could not load grayscale image at {image_path}")

print("\n--- 2. Testing with Pillow (PIL) ---")

# --- Pillow (PIL) ---
try:
    img_pil = Image.open(image_path)
    
    print("\n[Pillow (PIL) Image]")
    print(f"Type of object: {type(img_pil)}")
    # Note the order: (width, height)
    print(f"Size (w, h): {img_pil.size}") 
    
    # Unpack the .size tuple
    w_p, h_p = img_pil.size
    print(f"  Width (w):  {w_p} pixels")
    print(f"  Height (h): {h_p} pixels")
    
    # You can also get them directly
    print(f"  Width (from .width):  {img_pil.width} pixels")
    print(f"  Height (from .height): {img_pil.height} pixels")

    # Other properties
    print(f"Image Format: {img_pil.format}")
    print(f"Image Mode: {img_pil.mode}") # e.g., RGB, RGBA, L

except FileNotFoundError:
    print(f"\nError: PIL could not find image at {image_path}")