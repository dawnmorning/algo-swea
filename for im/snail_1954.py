import sys
sys.stdin = open('1954.txt')
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    snail = [[0]* n for _ in range(n)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    row = col = value = 0
    for i in range(1, n*n+1):
        snail[row][col] = i
        row += dr[value]
        col += dc[value]

        if row < 0 or row >= n or col < 0 or col >= n or snail[row][col] != 0:
            row -= dr[value]
            col -= dc[value]
            value = (value + 1) % 4
            row += dr[value]
            col += dc[value]

    print(f'#{tc}')
    for j in range(len(snail)):
        for k in range(len(snail)):
            print(snail[j][k], end = ' ')
        print()


