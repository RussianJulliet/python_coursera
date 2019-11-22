def CountSort(A):
    sort = [0] * 101
    for i in A:
        sort[i] += 1
    for k in range(len(sort)):
        print((str(k) + ' ') * sort[k], end='')


lis = list(map(int, input().split()))
CountSort(lis)
