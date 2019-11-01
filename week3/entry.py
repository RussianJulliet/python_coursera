s = str(input())
revert = s[::-1]
k = s.find('f')
t = revert.find('f')
tt = len(s) - 1 - t
if k != -1:
    if k != tt:
        print(k, tt)
    else:
        print(k)
