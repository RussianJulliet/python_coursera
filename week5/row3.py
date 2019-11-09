n = int(input())
A = 10 ** n - 1
B = 10 ** (n - 1)
for i in range(A, B - 1, -2):
    print(i, end=' ')
