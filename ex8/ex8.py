import cv2
import matplotlib.pyplot as plt
import numpy as np

# --- 1. Load the Original Image ---
# We use 'lena.png' since we have it in our folder.
# We load it in grayscale (flag = 0) as shown in the task.
original_image = cv2.imread('lena.png', 0)

# Check if the image was loaded correctly
if original_image is None:
    print("Error: Could not load 'lena.png'.")
    print("Please make sure 'lena.png' is in the same folder as the script.")
else:
    # --- 2. Create the Mask ---
    # 1. Create a black canvas with the same dimensions as the original
    #    dtype="uint8" means values from 0 to 255.
    mask = np.zeros(original_image.shape, dtype="uint8")

    # 2. Draw a white figure on the mask.
    # We use color '1' (not 255) as explained in the task,
    # so that multiplication works correctly (Image * 1 = Image).
    # (thickness=-1 means fill the shape).
    # The coordinates (150, 150) to (350, 350) are for the Lena image.
    cv2.rectangle(mask, (150, 150), (350, 350), 1, -1)

    # --- 3. Perform Multiplication ---
    # This multiplies the original image by the mask, pixel by pixel.
    # - Where mask is 0:  Image_Pixel * 0 = 0 (Black)
    # - Where mask is 1:  Image_Pixel * 1 = Image_Pixel (Original)
    result = cv2.multiply(original_image, mask)

    # --- 4. Display the Results ---
    plt.figure(figsize=(15, 5)) # Use a wide figure for 3 plots

    # Plot 1: Original Image
    plt.subplot(1, 3, 1)
    plt.imshow(original_image, cmap='gray')
    plt.title("Original Image (lena.png)")
    plt.axis('off')

    # Plot 2: The Mask
    plt.subplot(1, 3, 2)
    plt.imshow(mask, cmap='gray')
    plt.title("Mask (0s and 1s)")
    plt.axis('off')

    # Plot 3: The Result
    plt.subplot(1, 3, 3)
    plt.imshow(result, cmap='gray')
    plt.title("Result: Multiply(Image, Mask)")
    plt.axis('off')

    plt.show()