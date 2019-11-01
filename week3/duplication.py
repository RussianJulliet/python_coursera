s = str(input())
revert = s[::-1]
k = s.find('h')
t = revert.find('h')
tt = len(s) - 1 - t
# print(s[:tt])
# print(s[k + 1:])
ans = s[:tt] + s[k + 1:]
print(ans)
