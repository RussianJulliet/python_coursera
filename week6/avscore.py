import statistics


inFile = open('avscore_input.txt', 'r', encoding='utf-8-sig')
lines = inFile.readlines()
line = ''
score9 = []
score10 = []
score11 = []
for line in lines:
    lst = line.split()
    if lst[2] == '9':
        score9.append(int(lst[3]))
    if lst[2] == '10':
        score10.append(int(lst[3]))
    if lst[2] == '11':
        score11.append(int(lst[3]))
print(statistics.mean(score9), end=' ')
print(statistics.mean(score10), end=' ')
print(statistics.mean(score11), end=' ')
