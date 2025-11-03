import cv2

img = cv2.imread('image.png')

if img is not None:
    scale = 0.5
    small = cv2.resize(img, (0, 0), fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
    cv2.imshow('Image Output', small)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not load image.")
    print("Please make sure 'image.png' is in the same folder as the script.")
