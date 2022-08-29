import sys
sys.stdin = open('ladder.txt')
t = 10
for tc in range(1, t+1):
    a = input()
    ladder = [list(map(int, input().split()))for _ in range(100)]
    for i in range(100):
        for j in range(100):
            if ladder[99][j] == 2:
                col = j
                break
    row = 99
    while row != 0:
        if col > 0 and ladder[row][col-1] == 1:
            ladder[row][col] = 0
            col = col-1
        elif col < 99 and ladder[row][col+1] == 1:
            ladder[row][col] = 0
            col = col + 1
        elif ladder[row-1][col] == 1:
            row -= 1
    print(f'#{tc} {col}')