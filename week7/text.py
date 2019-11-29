with open('input.txt') as f:
    s = f.read()
lst = []
lst = s.split()
count_lines = {}
for i in lst:
    count_lines[i] = count_lines.get(i, 0) + 1
    print(count_lines[i] - 1, end=' ')
