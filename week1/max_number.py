A = int(input())
B = int(input())
X = A * (A // B)
Y = B * (B // A)
maxim = (X + Y) // (A // B + B // A)
print(maxim)
