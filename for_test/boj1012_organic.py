from collections import deque

def bfs(land,r,c):
    dr = [0,0,1,-1]
    dc = [1,-1,0,0]
    q = deque()
    q.append((r,c))
    land[r][c] = 0
    while q:
        r,c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < n and 0 <= nc < m:
                if land[nr][nc] == 1:
                    land[nr][nc] = 0
                    q.append((nr,nc))
    return

t = int(input())


for tc in range(1, t+1):
    cnt = 0
    n, m, k = map(int, input().split())
    land = [[0] * m for _ in range(n)]
    for _ in range(k):
        r, c = map(int, input().split())
        land[r][c]=1
    for a in range(n):
        for b in range(m):
            if land[a][b] == 1:
                bfs(land,a,b)
                cnt += 1
    print(cnt)