import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Create the Shapes ---

# Create a black canvas (300x300) and draw a white RECTANGLE
# A white-filled (-1) rectangle from (25,25) to (275, 275)
rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)

# Create a black canvas (300x300) and draw a white CIRCLE
# A white-filled (-1) circle centered at (150,150) with radius 150
circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)

# --- 2. Perform Logical Operations ---

# AND: Only the pixels that are ON (white) in BOTH images
bitwise_and = cv2.bitwise_and(rectangle, circle)

# OR: The pixels that are ON (white) in EITHER image
bitwise_or = cv2.bitwise_or(rectangle, circle)

# XOR: The pixels that are ON (white) in one, but NOT both
bitwise_xor = cv2.bitwise_xor(rectangle, circle)

# NOT: Inverts the pixels (white becomes black, black becomes white)
# The example uses the 'rectangle' image for this operation
bitwise_not = cv2.bitwise_not(rectangle)

# --- 3. Display the Results ---

# Set up a 2x3 grid for plotting
# (Your example code used (20,20), I'm using (15,10) as it fits a 2x3 grid better)
plt.figure(figsize=(15, 10))

# Plot 1: Rectangle (Top-Left)
plt.subplot(2, 3, 1)
plt.imshow(rectangle, cmap='gray')
plt.title("Rectangle")
plt.axis('off')

# Plot 2: Circle (Top-Middle)
plt.subplot(2, 3, 2)
plt.imshow(circle, cmap='gray')
plt.title("Circle")
plt.axis('off')

# Plot 3: AND (Top-Right)
plt.subplot(2, 3, 3)
plt.imshow(bitwise_and, cmap='gray')
plt.title("AND (Overlap)")
plt.axis('off')

# Plot 4: OR (Bottom-Left)
plt.subplot(2, 3, 4)
plt.imshow(bitwise_or, cmap='gray')
plt.title("OR (Union)")
plt.axis('off')

# Plot 5: XOR (Bottom-Middle)
plt.subplot(2, 3, 5)
plt.imshow(bitwise_xor, cmap='gray')
plt.title("XOR (Non-Overlapping)")
plt.axis('off')

# Plot 6: NOT (Bottom-Right)
plt.subplot(2, 3, 6)
plt.imshow(bitwise_not, cmap='gray')
plt.title("NOT (of Rectangle)")
plt.axis('off')

# Show the final window
plt.tight_layout() # Helps space out the titles
plt.show()