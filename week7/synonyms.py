n = int(input())
synonim = dict()
for i in range(n):
    syn1, syn2 = [str(s) for s in input().split()]
    synonim[syn1] = syn2
    synonim[syn2] = syn1
str = input()
print(synonim[str])
