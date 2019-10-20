n = int(input())
h = (n // 3600) % 24
mm = (n // 60) % 60
ss = n % 60
print(h, end=':')
print(mm // 10, end='')
print(mm % 10, end=':')
print(ss // 10, end='')
print(ss % 10)
