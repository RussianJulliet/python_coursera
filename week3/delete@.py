s = str(input())
while s.find('@') != -1:
    k = s.find('@')
    s = s[:k] + s[k + 1:]
print(s)
