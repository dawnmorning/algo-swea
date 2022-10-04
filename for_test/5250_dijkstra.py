import sys
sys.stdin = open('5250.txt')

def dfs():
    dr = [0,0,-1,1]
    dc = [1,-1,0,0]
    inf = 10 ** 6
    visited = [[inf] * n for _ in range(n)]
    visited[0][0] = 0
    q = []
    q.append(start)
    while q:
        r,c = q.pop(0)
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < n and 0 <= nc < n :
                extra = 0
                if arr[nr][nc] > arr[r][c]:
                    extra = arr[nr][nc] - arr[r][c]
                if visited[nr][nc] > visited[r][c] + extra + 1:
                    visited[nr][nc] = visited[r][c] + extra + 1
                    q.append((nr,nc))
    return visited[n-1][n-1]


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split()))for _ in range(n)]
    minV = 987654321
    start = (0,0)
    dfs()
    print(f'#{tc} {dfs()}')