import sys
sys.stdin = open('5188.txt')
def dfs(r, c):
    global start, minV
    if minV < start:
        return
    if r == n-1 and c == n-1:
        minV = start
    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < n and nc < n and (nr, nc) not in visited:
            visited.append((nr,nc))
            start += arr[nr][nc]
            dfs(nr, nc)
            visited.remove((nr,nc))
            start -= arr[nr][nc]
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split()))for _ in range(n)]
    minV = 99999
    visited = []
    dr = [0,1]
    dc = [1,0]

    start = arr[0][0]
    dfs(0,0)
    print(f'#{tc} {minV}')
