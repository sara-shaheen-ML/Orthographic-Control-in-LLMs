from wordfreq import top_n_list
import re
import csv

words = top_n_list("en", 25000)

rows = []
for rank, w in enumerate(words, start=1):
    w = w.lower()
    if re.fullmatch(r"[a-z]+", w):
        if rank <= 5000:
            band = "high"
        elif rank <= 15000:
            band = "medium"
        else:
            band = "low"
        rows.append((w, rank, band))

with open("words_25k_with_bands.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["word", "frequency_rank", "band"])
    writer.writerows(rows)

print(f"Wrote {len(rows)} words with frequency bands")
