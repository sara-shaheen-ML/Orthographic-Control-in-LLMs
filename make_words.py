from wordfreq import top_n_list
import re

# Get top 25,000 English words by frequency
words = top_n_list("en", 25000)

clean_words = []
for w in words:
    w = w.lower()
    # Keep only alphabetic words (paper-friendly)
    if re.fullmatch(r"[a-z]+", w):
        clean_words.append(w)

print(f"Kept {len(clean_words)} clean alphabetic words")

# Save to file
with open("words_25k.txt", "w", encoding="utf-8") as f:
    for w in clean_words:
        f.write(w + "\n")
