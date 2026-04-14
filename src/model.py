from tensorflow.keras import layers, Model, Input


def build_base_network(input_shape):
    input = Input(shape=input_shape)

    x = layers.Conv2D(32, (3,3), activation='relu')(input)
    x = layers.MaxPooling2D()(x)

    x = layers.Conv2D(64, (3,3), activation='relu')(x)
    x = layers.MaxPooling2D()(x)

    x = layers.Conv2D(128, (3,3), activation='relu')(x)
    x = layers.MaxPooling2D()(x)

    x = layers.Flatten()(x)
    x = layers.Dense(128, activation='relu')(x)

    return Model(input, x)


def build_siamese_model(input_shape):
    base_network = build_base_network(input_shape)

    input_a = Input(shape=input_shape)
    input_b = Input(shape=input_shape)

    feat_a = base_network(input_a)
    feat_b = base_network(input_b)

    # 🔥 Better comparison
    diff = layers.Subtract()([feat_a, feat_b])
    mul = layers.Multiply()([feat_a, feat_b])

    x = layers.Concatenate()([diff, mul])

    x = layers.Dense(128, activation='relu')(x)
    x = layers.Dense(64, activation='relu')(x)

    output = layers.Dense(1, activation='sigmoid')(x)

    return Model([input_a, input_b], output)