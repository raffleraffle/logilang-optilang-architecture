import hashlib

def sha256(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

def merkle_root(hashes):
    if not hashes:
        return None

    while len(hashes) > 1:
        if len(hashes) % 2 == 1:
            hashes.append(hashes[-1])

        new_level = []
        for i in range(0, len(hashes), 2):
            combined = hashes[i] + hashes[i + 1]
            new_level.append(sha256(combined))
        hashes = new_level

    return hashes[0]

if __name__ == "__main__":
    sample = ["event1", "event2", "event3"]
    hashed = [sha256(x) for x in sample]
    print("Merkle root:", merkle_root(hashed))
