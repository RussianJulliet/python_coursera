s = str(input())
t = len(s)
k = 0
count = 0
while count != t - 1:
    tm = s[:k + 1] + '*'
    p = s[k + 1:]
    s = tm + p
    k += 2
    count += 1
print(s)
