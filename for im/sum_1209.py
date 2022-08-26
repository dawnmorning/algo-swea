import sys
sys.stdin = open('1209.txt')
t = 10
for tc in range(1, t+1):
    tc = input()
    arr = [list(map(int,input().split()))for _ in range(100)]
    max_number = 0
    for i in range(100):
        row_max = 0
        col_max = 0
        for j in range(100):
            row_max += arr[i][j]
            col_max += arr[j][i]
        if max_number < row_max:
            max_number = row_max
        if max_number < col_max:
            max_number = col_max
    daegak_max = 0
    for i in range(100):
        daegak_max += arr[i][i]
    if daegak_max > max_number:
        max_number = daegak_max
    print(f'#{tc} {max_number}')

