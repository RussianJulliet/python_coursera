import sys

words = set()
for line in sys.stdin:
    lst = line.strip().split()
    for word in lst:
        words.add(word)
print(len(words))
