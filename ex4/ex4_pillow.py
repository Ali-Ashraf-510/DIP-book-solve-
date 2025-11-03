from PIL import Image

# 1. Load the image
try:
    img = Image.open('lena.png')
    img.show(title="Original Image (PIL)") # Show original
except FileNotFoundError:
    print("Error: Could not find 'lena.png'.")
    print("Make sure it's in the same folder as your script.")
    exit()

# 2. Define the crop box (left, upper, right, lower)
# For a 250x250 crop from the center of a 512x512 image
center_x, center_y = 256, 256
half_width, half_height = 125, 125

left = center_x - half_width     # 256 - 125 = 131
upper = center_y - half_height   # 256 - 125 = 131
right = center_x + half_width    # 256 + 125 = 381
lower = center_y + half_height   # 256 + 125 = 381

box = (left, upper, right, lower)

# 3. Crop the image
img_cropped = img.crop(box)

# 4. Save and show the cropped image
img_cropped.save('myimage_cropped_pil.png')
img_cropped.show(title="Cropped Image (PIL)")

print(f"Original size: {img.size}")
print(f"Cropped size: {img_cropped.size}")