import sys
sys.stdin = open('1210.txt')
t = 10
for tc in range(1, t+1):
    tc = input()
    ladder = [list(map(int,input().split())) for _ in range(100)]
    dr = [0,0,-1]
    dc = [-1,1,0]
    for i in range(100):
        for j in range(100):
            if ladder[i][j] == 2:
                si, sj = [i,j]
    while si != 0:
        for k in range(3):
            ni = si + dr[k]
            nj = sj + dc[k]
            if 0 <= ni < 100 and 0 <= nj < 100:
                if ladder[ni][nj] == 1:
                    ladder[si][sj] = 0
                    si = ni
                    sj = nj
    print(f'#{tc} {sj}')
