n = int(input())
string = ''
while n > 0:
    string += str(n % 10)
    n //= 10
print(string)
