import numpy as np
from .dataset_loader import load_dataset
from .pair_generator import create_pairs
from .preprocess import load_pair
from .model import build_siamese_model
from .config import DATA_PATH, IMAGE_SIZE, BATCH_SIZE, EPOCHS


def train():
    dataset = load_dataset(DATA_PATH)
    pairs, labels = create_pairs(dataset, max_pairs_per_person=50)

    X1, X2 = [], []

    for pair in pairs:
        img1, img2 = load_pair(pair)
        X1.append(img1)
        X2.append(img2)

    X1 = np.array(X1)
    X2 = np.array(X2)
    y = np.array(labels)

    model = build_siamese_model((100, 150, 1))  # height, width, channel
    
    model.compile(
        loss='binary_crossentropy',
        optimizer='adam',
        metrics=['accuracy']
    )

    model.fit([X1, X2], y, batch_size=BATCH_SIZE, epochs=EPOCHS)

    model.save("models/signature_model.h5")