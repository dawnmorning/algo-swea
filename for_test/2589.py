from collections import deque
def bfs(r,c,cnt):
    pre_cnt = -1
    q = deque()
    q.append((r,c,cnt))
    visited[r][c] = 1
    while q:
        r,c,idx = q.popleft()
        if pre_cnt < idx:
            pre_cnt = idx
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < n and 0 <= nc < m and treasure[nr][nc] == 'L':
                q.append((nr,nc,idx+1))
                visited[nr][nc] = 1
    return pre_cnt


n, m = map(int, input().split())
treasure = [list(input()) for _ in range(n)]

dr = [0,0,1,-1]
dc = [1,-1,0,0]

mx = -1
for r in range(n):
    for c in range(m):
        if treasure[r][c] == 'L':
            visited = [[0] * m for _ in range(n)]
            mx = max(mx, bfs(r,c,0))
print(mx)
