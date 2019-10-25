# count1 = 1
# count2 = 1
# max_count1 = 0
# max_count2 = 0
# m = int(input())
# s = m
# while m != 0:
#     s = m
#     # print(s)
#     m = int(input())
#     # print(m)
#     if s > m:
#         count1 += 1
#     elif s == m:
#         count1 = 0
#     if max_count1 < count1:
#         max_count1 = count1
#     if s < m:
#         count2 += 1
#     elif s == m:
#         count2 = 0
#     if max_count2 < count2:
#         max_count2 = count2
# if max_count1 >= max_count2:
#     print(max_count1)
# else:
#     print(max_count2)
x1 = int(input())
x2 = int(input())
n_max = 1
n = 1
while 0 == 0:
    if x2 == 0 or x1 == 0:
        break
    while x1 > x2:
        if x2 == 0:
            break
        n += 1
        if n > n_max:
            n_max = n
            x1 = x2
            x2 = int(input())
        else:
            x1 = x2
            x2 = int(input())
    n = 1
    while x1 < x2:
        n += 1
        if n > n_max:
            n_max = n
            x1 = x2
            x2 = int(input())
        else:
            x1 = x2
            x2 = int(input())
    n = 1
    while x1 == x2:
        n = 1
        x1 = x2
        x2 = int(input())
print(n_max)
