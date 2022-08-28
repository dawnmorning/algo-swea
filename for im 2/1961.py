import sys
sys.stdin = open('1961.txt')
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split()))for _ in range(n)]
    arr90 = [[0] * n for _ in range(n)]
    arr180 = [[0] * n for _ in range(n)]
    arr270 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr90[i][j] = arr[n-1-j][i]
    for i in range(n):
        for j in range(n):
            arr180[i][j] = arr90[n-1-j][i]
    for i in range(n):
        for j in range(n):
            arr270[i][j] = arr180[n-1-j][i]
    print(f'#{tc}')
    for i in range(n):
        for a in range(n):
            print(arr90[i][a], end = '')
        print(end=' ')
        for b in range(n):
            print(arr180[i][b], end ='')
        print(end=' ')
        for c in range(n):
            print(arr270[i][c], end = '')
        print(end=' ')
        print()