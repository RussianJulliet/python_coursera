N, M = [int(s) for s in input().split()]
anna = set()
borya = set()
for i in range(N):
    x = int(input())
    anna.add(x)
for k in range(M):
    x = int(input())
    borya.add(x)
print(len(anna & borya))
print(*sorted(anna & borya))
print(len(anna - borya))
print(*sorted(anna - borya))
print(len(borya - anna))
print(*sorted(borya - anna))
