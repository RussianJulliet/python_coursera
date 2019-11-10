n = int(input())
print('+___ ' * n)
string = ''
for i in range(1, n + 1):
    string = string + '|' + str(i) + ' / '
print(string)
string1 = '|__\\ '
print(string1 * n)
print('|    ' * n)
