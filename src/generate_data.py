import os
import cv2
import numpy as np

#script to generate random images for dataset
for i in range(50):
    img = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
    label = "defective" if i % 2 == 0 else "non_defective"
    cv2.imwrite(f"dataset/{label}/{i}.png", img)