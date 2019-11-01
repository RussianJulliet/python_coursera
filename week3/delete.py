s = str(input())
revert = s[::-1]
k = s.find('h')
t = revert.find('h')
tt = len(s) - 1 - t
answer = s[:k] + s[tt + 1:]
print(answer)
