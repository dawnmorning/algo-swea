import sys
sys.stdin = open('1961.txt')
t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr_90 = [[0 for _ in range(n)] for _ in range(n)]
    arr_180 = [[0 for _ in range(n)] for _ in range(n)]
    arr_270 = [[0 for _ in range(n)] for _ in range(n)]
    print(f'#{tc}')
    for i in range(n):
        for j in range(n):
            arr_90[i][j] = arr[n-1-j][i]
        print(arr_90,end = '')
        for j in range(n):
            arr_180[i][j] = arr_90[n-1-j][i]
        print(arr_180, end= '')
        for j in range(n):
            arr_270[i][j] = arr_180[n-1-j][i]
            print(arr_270, end='')
        print()

