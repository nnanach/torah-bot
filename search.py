import csv

CSV_PATH = "torah_lookup.csv"

def search(query, limit=5):
    q = query.lower()
    scored = []

    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            text = row["text"].lower()

            # simple relevance score
            score = text.count(q)

            if score > 0:
                scored.append((score, row))

    scored.sort(key=lambda x: x[0], reverse=True)

    return [r for _, r in scored[:limit]]
