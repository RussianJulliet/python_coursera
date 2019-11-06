def cnk(n, k):
    if k == 1:
        return n
    elif k == n or k == 0:
        return 1
    else:
        return cnk(n - 1, k) + cnk(n - 1, k - 1)


n = int(input())
k = int(input())
print(cnk(n, k))
