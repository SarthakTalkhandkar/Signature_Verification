import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "data", "CEDAR", "CEDAR")

IMAGE_SIZE = (150, 100)  # width, height for OpenCV   # standard for signature models
BATCH_SIZE = 16
EPOCHS = 15