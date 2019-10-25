X = int(input())
Y = int(input())
track = X
day = 1
while X < Y:
    X = 1.1 * X
    track = track + X
    day = day + 1
print(day)
