n = int(input())
term1 = 0
term2 = 1
i = 0
fib = 0
while i < n:
    term1 = term2
    term2 = fib
    fib = term1 + term2
    i += 1
print(fib)
