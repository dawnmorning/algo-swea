import sys
sys.stdin = open('1954.txt')
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    snail = [[0] * n for _ in range(n)]
    move_r = [0,1,0,-1]
    move_c = [1,0,-1,0]
    x = y = 0
    z = 0
    for i in range(1, n*n+1):
        snail[x][y] = i
        x += move_r[z]
        y += move_c[z]
        if x < 0 or x >= n or y < 0 or y >= n or snail[x][y] != 0:
            x -= move_r[z]
            y -= move_c[z]
            z = (z + 1) % 4
            x += move_r[z]
            y += move_c[z]
    print(f'#{tc}')
    for j in range(n):
        for k in range(n):
            print(snail[j][k], end= ' ')
        print()
