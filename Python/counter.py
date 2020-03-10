from collections import Counter


words = "if there was there was but if there was not there was not".split()
counts = Counter(words)

print(counts)
print(counts.most_common(2))
