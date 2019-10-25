# A = int(input())
# term1 = 0
# term2 = 1
# i = 0
# fib = 0
# s = -1
# if A == 0:
#     print(0)
# elif A == 1:

#     print(1, 2)
# else:
#     while i < A:
#         fib = term1 + term2
#         term1 = term2
#         term2 = fib
#         if A == fib:
#             s = fib
#             print(i + 2)
#         i += 1
#     if s == -1:
#         print(s)
A = int(input())
f1 = 1
f2 = 1
i = 2
if A == 0:
    print(0)
elif A == 1:

    print(1, 2)
else:
    while f2 < A:
        tmp = f2
        f2 += f1
        f1 = tmp
        i += 1
    if f2 == A:
        print(i)
    else:
        print(-1)
