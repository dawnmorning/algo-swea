import sys
sys.stdin = open('1767.txt')
import copy

def perfect_find(cnt, temp, connect, where, maxynoth):
    global min_len
    global total_core

    r, c = where[cnt]
    dr = [0,0,1,-1]
    dc = [-1,1,0,0]
    for k in range(4):
        deep_maxynoth = copy.deepcopy(maxynoth)
        nr = r + dr[k]
        nc = c + dc[k]
        move = 0
        while 0 <= nr < n and 0 <= nc < n:
            if deep_maxynoth[nr][nc] == 1:
                move = 0
                break
            else:
                move += 1
                deep_maxynoth[nr][nc] = 1
                nr = nr + dr[k]
                nc = nc + dc[k]
        if move == 0:
            continue
        else:
            perfect_find(cnt+1,temp+move,connect+1,where,deep_maxynoth)

    perfect_find(cnt+1, temp, connect, where, maxynoth)


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maxynoth = [list(map(int, input().split())) for _ in range(n)]
    where = []
    min_len = 9876543210
    total_core = 0
    for i in range(1, n-1):
        for j in range(1,n-1):
            if maxynoth[i][j] == 1:
                where.append((i,j))
    perfect_find(0,0,0,where,maxynoth)

