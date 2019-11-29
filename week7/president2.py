from collections import Counter

with open("input.txt", "rt", encoding="utf-8") as f:
    candidates = Counter(map(str.strip, f))

voices = sum(candidates.values())

with open("output.txt", "wt", encoding="utf-8") as f:
    percent = candidates.most_common(1)[0][1] / voices * 100
    if percent > 50:
        print(candidates.most_common(1)[0][0], file=f)
    else:
        for name, _ in candidates.most_common(2):
            print(name, file=f)
