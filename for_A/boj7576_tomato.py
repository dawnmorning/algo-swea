from collections import deque
m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]
res = 0
q = deque([])
for r in range(n):
    for c in range(m):
        if box[r][c] == 1:
            q.append([r,c])

def bfs():
    while q:
        x, y = q.popleft()
        for k in range(4):
            nr = x + dr[k]
            nc = y + dc[k]
            if 0 <= nr < n and  0 <= nc < m and box[nr][nc] == 0:
                box[nr][nc] = box[x][y] + 1
                q.append([nr,nc])
bfs()

for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res,max(i))
print(res - 1)
