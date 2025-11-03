import cv2
import matplotlib.pyplot as plt

# --- 1. Load the image ---
# NOTE: Using the full, absolute path to prevent "file not found" errors
image_path = 'lena.png'

# Load the image in grayscale (flag = 0)
lena = cv2.imread(image_path, 0)

# --- 2. Check if image loaded ---
if lena is None:
    print(f"Error: Could not load image from {image_path}")

else:
    # --- 3. Perform Subtraction ---
    # We will subtract the constant value 128 from all pixels
    # cv2.subtract is "safe" - any pixel that goes below 0 will be set to 0
    # For example: 50 - 128 = 0 (not -78)
    subtracted_image = cv2.subtract(lena, 128)

    # --- 4. Display the results ---
    plt.figure(figsize=(15, 8))

    # Plot 1: The original image
    plt.subplot(1, 2, 1)
    plt.imshow(lena, cmap='gray')
    plt.title("Original Lena (Grayscale)")
    plt.axis('off')

    # Plot 2: The subtracted image
    plt.subplot(1, 2, 2)
    plt.imshow(subtracted_image, cmap='gray')
    plt.title("Result: subtract(lena, 128)")
    plt.axis('off')

    plt.show()