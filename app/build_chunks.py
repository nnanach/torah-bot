import os
import csv

TORAH_DIR = "/home/user/Documents/Torah"
OUTPUT = "torah_lookup.csv"

def chunk_text(text, size=800, overlap=100):
    chunks = []
    i = 0
    while i < len(text):
        chunks.append(text[i:i+size])
        i += size - overlap
    return chunks

rows = []
doc_id = 0

for root, dirs, files in os.walk(TORAH_DIR):
    for f in files:
        if f.endswith(".html") or f.endswith(".txt"):
            path = os.path.join(root, f)

            with open(path, "r", encoding="utf-8", errors="ignore") as file:
                text = file.read()

            chunks = chunk_text(text)

            for c in chunks:
                rows.append([
                    doc_id,
                    c,
                    path,
                    "torah"
                ])
                doc_id += 1

with open(OUTPUT, "w", newline="", encoding="utf-8") as out:
    writer = csv.writer(out)
    writer.writerow(["id", "text", "source_path", "tags"])
    writer.writerows(rows)

print("DONE:", len(rows))
