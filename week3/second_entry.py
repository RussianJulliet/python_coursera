s = str(input())
k = s.find('f')
revert = s[::-1]
st = s[k + 1:]
t = revert.find('f')
tt = len(s) - 1 - t
if k != -1:
    if k != tt:
        count = k
        while st[0] != 'f':
            st = st[1:]
            count += 1
        print(count + 1)
    else:
        print(-1)
else:
    print(-2)
