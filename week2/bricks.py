A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
if B >= A:
    (A, B) = (B, A)
if C >= A:
    (A, C) = (C, A)
if C >= B:
    (B, C) = (C, B)
if ((B <= D) and (C <= E)) or ((C <= D) and (B <= E)):
    print('YES')
else:
    print('NO')
