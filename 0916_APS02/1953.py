import sys

sys.stdin = open('1953.txt')

def bfs(n,m):
    visited[r][c] = 1
    q = [(r, c)]
    direct = [(0,-1), (-1,0), (0,1), (1,0)]
    pipe = [[],[0,1,2,3],[1,3],[0,2],[1,2],[3,2],[3,0],[1,0]]
    while q:
        x, y = q.pop(0)
        z = pipe[tunnel[x][y]]
        if z == []:
            continue
        for i in z:
            di, dj = direct[i]
            nx, ny = x + di, y + dj
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and tunnel[nx][ny] != 0:
                next = pipe[tunnel[nx][ny]]
                for j in next:
                    mx, my = nx + direct[j][0], ny + direct[j][1]
                    if mx == x and my == y:
                        q.append((nx,ny))
                        visited[nx][ny] = visited[x][y] + 1

t = int(input())
for tc in range(1, t+1):
    n, m, r, c, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]* m for _ in range(n)]
    bfs(n,m)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if 0 < visited[i][j] <= L:
                cnt += 1
    print(f'#{tc} {cnt}')
