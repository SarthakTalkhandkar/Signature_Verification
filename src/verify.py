import numpy as np
from tensorflow.keras.models import load_model
from .preprocess import preprocess_image

MODEL_PATH = "models/signature_model.h5"

model = load_model(MODEL_PATH, safe_mode=False)

def verify_signature(img1_path, img2_path):
    img1 = preprocess_image(img1_path)
    img2 = preprocess_image(img2_path)

    img1 = np.expand_dims(img1, axis=0)
    img2 = np.expand_dims(img2, axis=0)

    prediction = model.predict([img1, img2])[0][0]

    return prediction