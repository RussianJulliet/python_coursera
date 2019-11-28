n = int(input())
max_set = set()
yes_set = set()
flagg = 0
for i in range(1, n):
    max_set.add(i)
lst_number = []
while lst_number != ['HELP']:
    lst_number = input().split()
    if lst_number != ['HELP']:
        for s in range(len(lst_number)):
            lst_number[s] = int(lst_number[s])
        # print(type(lst_number[0]))
        string = input()
        if string == 'NO':
            max_set = max_set - set(lst_number)
        else:
            for i in lst_number:
                if flagg == 0:
                    yes_set.add(int(i))
                    flagg = 1
                yes_set = yes_set & set(lst_number)
                print(*yes_set)
print(*max_set)
print(*sorted(max_set & yes_set))
