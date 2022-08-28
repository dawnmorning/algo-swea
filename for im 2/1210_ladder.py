import sys
sys.stdin=open('1210.txt')
t = 10
for tc in range(1, t+1):
    a = input()
    ladder = [list(map(int, input().split()))for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if ladder[i][j] == 2:
                row, col = i, j
                break
    dr = [-1, 0, 0]
    dc = [0, -1, 1]
    while row != 0:
        for k in range(3):
            next_row = row + dr[k]
            next_col = col + dc[k]
            if 0 <= next_row < 100 and 0 <= next_col <100 and ladder[next_row][next_col] != 0:
                if ladder[next_row][next_col] == 1:
                    ladder[row][col] = 0
                    row = next_row
                    col = next_col
    print(f'#{tc} {col}')
