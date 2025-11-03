import cv2
import matplotlib.pyplot as plt
import numpy as np

# --- 1. Create two simple images ---
# These are black images to start
img1_sub = np.zeros((300, 300), dtype="uint8")
img2_sub = np.zeros((300, 300), dtype="uint8")

# Draw a white rectangle on BOTH images (the 'original' part)
cv2.rectangle(img1_sub, (50, 50), (200, 200), 255, -1)
cv2.rectangle(img2_sub, (50, 50), (200, 200), 255, -1)

# Now, add a "change" (a circle) ONLY to the second image
cv2.circle(img2_sub, (200, 200), 75, 255, -1)

# --- 2. Subtract the images ---
# This will subtract img1 from img2. 
# The overlapping rectangle will become 0 (black).
# The new circle will remain (255 - 0 = 255).
changes = cv2.subtract(img2_sub, img1_sub)

# --- 3. Display the results ---
plt.figure(figsize=(15, 5))

# Plot 1: The "Before" image
plt.subplot(1, 3, 1)
plt.imshow(img1_sub, cmap='gray')
plt.title("Image 1 (Before)")
plt.axis('off')

# Plot 2: The "After" image
plt.subplot(1, 3, 2)
plt.imshow(img2_sub, cmap='gray')
plt.title("Image 2 (After)")
plt.axis('off')

# Plot 3: The "Changes"
plt.subplot(1, 3, 3)
plt.imshow(changes, cmap='gray')
plt.title("Result: subtract(img2, img1)")
plt.axis('off')

plt.show()