N = int(input())
CD = N % 100
AB = N // 100
CD = CD // 10 + CD % 10 * 10
print(AB - CD + 1)
