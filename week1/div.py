a = int(input())
b = int(input())
param = 0**(a % b)
print('YES' * param + 'NO' * ((-1) * param + 1))
