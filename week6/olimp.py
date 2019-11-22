class Man:
    lastname = ''
    score = 0


n = int(input())
people = []
for i in range(n):
    lst = input().split()
    man = Man()
    man.lastname = lst[0]
    man.score = lst[1]
    people.append(man)
people.sort(key=lambda mans: -int(mans.score))
for man in people:
    print(man.lastname)
