def listAverage(list):
    sum = 0
    for i in list:
        sum += i
    return sum / len(list)


classes = {}
inFile = open('input.txt', 'r', encoding='utf-8')
for line in inFile:
    grade, mark = line.split()[2:]
    if grade in classes:
        classes[grade].append(int(mark))
    else:
        classes[grade] = [int(mark)]

for i in range(9, 12):
    print(listAverage(classes[str(i)]), end=' ')
