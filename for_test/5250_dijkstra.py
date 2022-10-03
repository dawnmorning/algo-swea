import sys
sys.stdin = open('5250.txt')

def dfs():
    q = []
    q.append((0,0))
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    while q:
        r,c = q.pop(0)
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                extra = 0
                if height[nr][nc] > height[r][c]:
                    extra = height[nr][nc] - height[r][c]:
                if visited[nr][nc] > visited[r][c] + extra +1:
                    visited[nr][nc] = visited[r][c] + extra + 1:
                    q.append((nr,nc))
    return visited[n-1][n-1]
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    height= [list(map(int, input().split())) for _ in range(n)]
    inf = 10 ** 6
    visited = [[inf] * n for _ in range(n)]
    visited[0][0] = 0
    print(f'#{tc} {dfs()}')
