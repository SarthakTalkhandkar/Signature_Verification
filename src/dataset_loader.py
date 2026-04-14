import os

def load_dataset(base_path):
    data = {}

    for person_id in os.listdir(base_path):
        person_path = os.path.join(base_path, person_id)

        if not os.path.isdir(person_path):
            continue

        originals = []
        forgeries = []

        for file in os.listdir(person_path):
            file_path = os.path.join(person_path, file)

            if file.startswith("original"):
                originals.append(file_path)

            elif file.startswith("forgeries"):
                forgeries.append(file_path)

        data[person_id] = {
            "originals": originals,
            "forgeries": forgeries
        }

    return data