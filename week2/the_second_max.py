n = int(input())
first_maxim = 0
second_maxim = 0
while n != 0:
    if n >= first_maxim:
        second_maxim = first_maxim
        first_maxim = n
    if first_maxim > n >= second_maxim:
        second_maxim = n
    n = int(input())
print(second_maxim)
