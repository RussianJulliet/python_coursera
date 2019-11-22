inFile = open('exam_input.txt', 'r', encoding='utf8')
k = inFile.readline()
lines = inFile.readlines()
outFile = open('exam_output.txt', 'w', encoding='utf8')
line = []
scores = []
for line in lines:
    lst = line.strip().split()
    if int(lst[-3]) > 40 and int(lst[-2]) > 40 and int(lst[-1]) > 40:
        score = int(lst[-3]) + int(lst[-2]) + int(lst[-1])
        print(int(lst[-3]))
        print(int(lst[-2]))
        print(int(lst[-1]))
        scores.append(score)
print(len(scores))
scores.sort(reverse=True)
if int(k) == 0:
    print(0, file=outFile)
else:
    if int(k) >= len(scores) or len(scores) == 0:
        print(0, file=outFile)
    elif scores[int(k) - 1] == scores[0]:
        print(1, file=outFile)
    else:
        if scores[int(k) - 1] != scores[int(k)]:
            print(scores[int(k) - 1], file=outFile)
        else:
            print(scores[int(k) - 2], file=outFile)
