import sys
sys.stdin = open('5188.txt')

def dfs(r,c):
    global minV,start

    if minV < start:
        return

    if r == c == n-1:
        minV = start

    dr = [0,1]
    dc = [1,0]
    for k in range(2):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in visited:
            visited.append((nr,nc))
            start = start + arr[nr][nc]
            dfs(nr,nc)
            visited.remove((nr,nc))
            start -= arr[nr][nc]

t = int(input())
for tc in range(1, t+1):
    visited = []
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    minV = 10000
    start = arr[0][0]
    dfs(0,0)
    print(f'#{tc} {minV}')