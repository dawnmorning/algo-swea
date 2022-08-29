import sys
sys.stdin = open('12712.txt')
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    fly = [list(map(int, input().split()))for _ in range(n)]
    di1 = [0,1,0,-1]
    dj1 = [1,0,-1,0]
    #대각 방향 (x자)
    di2 = [1, 1,-1,-1]
    dj2 = [1,-1,-1,1]
    maxV = 0
    for i in range(n):
        for j in range(n):
            cnt1 = fly[i][j]  #i j를 중심으로
            for k in range(4):
                for z in range(1, m):  #좌우로 2씩만 더 가면 되니까
                    next_i = i + di1[k] * z
                    next_j = j + dj1[k] * z
                    if 0 <= next_i < n and 0 <= next_j < n:
                        cnt1 += fly[next_i][next_j]
            if maxV < cnt1:
                maxV = cnt1

            cnt2 = fly[i][j]
            for di, dj in [[1,1],[1,-1],[-1,-1], [-1,1]]:
                for z in range(1,m):
                    ni, nj = i+di * z, j+dj * z
                    if 0 <= ni < n and 0 <= nj < n:
                        cnt2 += fly[ni][nj]
            if maxV < cnt2:
                maxV = cnt2
    print(f'#{tc} {maxV}')
