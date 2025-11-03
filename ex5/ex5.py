import cv2
import matplotlib.pyplot as plt
import os

script_dir = os.path.dirname(__file__)

tom_path = os.path.join('jj.png')
jerry_path = os.path.join('tt.png')

tom = cv2.imread(tom_path)
jerry = cv2.imread(jerry_path)

if tom is None:
    print(f"Error: Could not load {tom_path}")
    print("Make sure 'jj.png' is in the same folder as the script.")
elif jerry is None:
    print(f"Error: Could not load {jerry_path}")
    print("Make sure 'tt.png' is in the same folder as the script.")
else:
    tom = cv2.cvtColor(tom, cv2.COLOR_BGR2RGB)
    jerry = cv2.cvtColor(jerry, cv2.COLOR_BGR2RGB)

    if tom.shape != jerry.shape:
        print(f"Warning: Image sizes do not match! Tom: {tom.shape}, Jerry: {jerry.shape}")
        print("Resizing 'jerry' to match 'tom'.")
        
        height = tom.shape[0]
        width = tom.shape[1]
        
        jerry = cv2.resize(jerry, (width, height))

    tANDJ = cv2.add(tom, jerry)

    plt.figure(figsize=(20, 20))

    plt.subplot(1, 3, 1)
    plt.imshow(tom)
    plt.title("Tom (jj.png)")
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(jerry)
    plt.title("Jerry (tt.png)")
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(tANDJ)
    plt.title("Result: cv2.add(tom, jerry)")
    plt.axis('off')

    plt.show()
