class Man:
    lastname = ''
    name = ''
    score = 0


inFile = open('sort_input.txt', 'r', encoding='utf8')
lines = inFile.readlines()
outFile = open('sort_output.txt', 'w', encoding='utf8')
line = []
people = []
for line in lines:
    lst = line.split()
    man = Man()
    man.lastname = lst[0]
    man.name = lst[1]
    man.score = lst[3]
    people.append(man)
people.sort(key=lambda mans: mans.lastname)
for man in people:
    print(man.lastname, man.name, man.score, file=outFile)
inFile.close()
outFile.close()
