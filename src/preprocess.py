import cv2
import numpy as np
from .config import IMAGE_SIZE

def preprocess_image(image_path):
    img = cv2.imread(image_path)

    # Convert to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Resize
    img = cv2.resize(img, IMAGE_SIZE)

    # Threshold (remove noise)
    _, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

    # Normalize
    img = img / 255.0

    # Add channel dimension
    img = np.expand_dims(img, axis=-1)

    return img


def load_pair(pair):
    img1 = preprocess_image(pair[0])
    img2 = preprocess_image(pair[1])

    return img1, img2