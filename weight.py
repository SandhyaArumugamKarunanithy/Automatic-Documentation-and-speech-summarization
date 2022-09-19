import re
from collections import Counter

with open('input.txt') as f:
    sentence = f.read()

words = re.findall(r'\w+', sentence)
word_counts = Counter(words)
print word_counts
