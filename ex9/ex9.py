import cv2
import matplotlib.pyplot as plt
import numpy as np

# --- 1. Create the two images ---
# We will create 400x400 images
height, width = 400, 400

# Create img1 (Objects + Shadow)
# Start with a light gray background (value 200)
img1 = np.full((height, width), 200, dtype=np.uint8)

# Add some dark "dots" (value 50)
cv2.circle(img1, (100, 100), 30, 50, -1)
cv2.circle(img1, (300, 100), 30, 50, -1)
cv2.circle(img1, (100, 300), 30, 50, -1)
cv2.circle(img1, (300, 300), 30, 50, -1)

# Create img2 (The "Illumination/Shadow" Map)
# Start with a white background (value 255)
img2 = np.full((height, width), 255, dtype=np.uint8)

# Now, create a gradient shadow and apply it to BOTH images
# This will be a float-based operation
img1_float = img1.astype(np.float32)
img2_float = img2.astype(np.float32)

for i in range(width):
    # Create a shadow factor that goes from 1.0 (no shadow) to 0.3 (dark)
    shadow = 1.0 - (i / width) * 0.7 
    
    # Apply the shadow to both images
    img1_float[:, i] = img1_float[:, i] * shadow
    img2_float[:, i] = img2_float[:, i] * shadow

# Convert back to uint8 for display
img1_shadowed = img1_float.astype(np.uint8)
img2_shadow_map = img2_float.astype(np.uint8)


# --- 2. Perform the Division ---
# To avoid "division by zero", we use float images
# and add a tiny number (epsilon) to the denominator.
img1_norm = img1_shadowed.astype(np.float32)
img2_norm = img2_shadow_map.astype(np.float32)

epsilon = 1e-5 # A very small number
# This is the (img1 / img2) operation from your book
result = img1_norm / (img2_norm + epsilon)

# The result is a float (0.0-1.0), which imshow handles fine

# --- 3. Display the Results ---
plt.figure(figsize=(15, 5)) # A 1x3 plot looks better as (15, 5)

# Plot 1: Original Image with Shadow
plt.subplot(131)
plt.imshow(img1_shadowed, cmap='gray')
plt.title("Image 1 (Objects + Shadow)")
plt.axis('off')

# Plot 2: Illumination/Shadow Map
plt.subplot(132)
plt.imshow(img2_shadow_map, cmap='gray')
plt.title("Image 2 (Shadow Map)")
plt.axis('off')

# Plot 3: Result (Division)
plt.subplot(133)
plt.imshow(result, cmap='gray')
plt.title("Result: img1 / img2 (Shadow Removed)")
plt.axis('off')

plt.show()