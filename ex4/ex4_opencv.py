import cv2

# 1. Load the image
image = cv2.imread('lena.png')

if image is None:
    print("Error: Could not find 'lena.png'.")
    print("Make sure it's in the same folder as your script.")
    exit()

# 2. Show the original image
cv2.imshow("Original Image (OpenCV)", image)

# 3. Define the crop region [startY:endY, startX:endX]
# We use the same pixel values as the PIL example
startY = 131
endY = 381
startX = 131
endX = 381

# 4. Crop the image using array slicing
crop_image = image[startY:endY, startX:endX]

# 5. Save and show the cropped image
cv2.imwrite('myimage_cropped_opencv.png', crop_image)
cv2.imshow("Cropped Image (OpenCV)", crop_image)

print(f"Original shape: {image.shape}")
print(f"Cropped shape: {crop_image.shape}")

# 6. Wait for a key press to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()