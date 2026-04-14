import random
import itertools

def create_pairs(dataset, max_pairs_per_person=50):
    pairs = []
    labels = []

    person_ids = list(dataset.keys())

    for person_id, data in dataset.items():
        originals = data["originals"]
        forgeries = data["forgeries"]

        genuine_pairs = []
        forged_pairs = []

        # ✅ Genuine pairs
        for img1, img2 in itertools.combinations(originals, 2):
            genuine_pairs.append(([img1, img2], 1))

        # ❌ Forgery pairs (same person)
        for orig in originals:
            for forg in forgeries:
                forged_pairs.append(([orig, forg], 0))

        # ❌ Different person pairs
        other_person = random.choice([p for p in person_ids if p != person_id])
        other_originals = dataset[other_person]["originals"]

        for orig in originals:
            other_img = random.choice(other_originals)
            forged_pairs.append(([orig, other_img], 0))

        # 🔥 BALANCE DATA
        min_len = min(len(genuine_pairs), len(forged_pairs))

        genuine_pairs = random.sample(genuine_pairs, min_len)
        forged_pairs = random.sample(forged_pairs, min_len)

        person_pairs = genuine_pairs + forged_pairs

        random.shuffle(person_pairs)

        # limit
        person_pairs = person_pairs[:max_pairs_per_person]

        for pair, label in person_pairs:
            pairs.append(pair)
            labels.append(label)

    return pairs, labels