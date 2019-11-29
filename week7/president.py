candidates = {}
voices = 0

with open("input.txt", "rt", encoding="utf-8") as f:
    for name in map(str.strip, f):
        #         candidates[name] = candidates.setdefault(name, 0) + 1
        candidates[name] = candidates.get(name, 0) + 1
        voices += 1

candidates = sorted(candidates.items(), key=lambda x: x[1], reverse=True)

with open("output.txt", "wt", encoding="utf-8") as f:
    percent = candidates[0][1] / voices * 100
    if percent > 50:
        print(candidates[0][0], file=f)
    else:
        for name, _ in candidates[:2]:
            print(name, file=f)
