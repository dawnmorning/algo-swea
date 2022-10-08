import sys
sys.stdin = open('1949.txt')
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
def find_road(r,c,cnt):
    global sabjil
    global maxlen

    if maxlen < cnt:
        maxlen = cnt

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < n and 0<= nc < n and visited[nr][nc] == 0 :
            if maps[nr][nc] < maps[r][c]:
                visited[nr][nc] = 1
                find_road(nr,nc,cnt+1)
                visited[nr][nc] = 0
            elif maps[nr][nc] >= maps[r][c] and sabjil == False:
                for a in range(1, K+1):
                    maps[nr][nc] -= a
                    sabjil = True
                    if maps[nr][nc] < maps[r][c]:
                        visited[nr][nc] = 1
                        find_road(nr,nc,cnt+1)
                        visited[nr][nc] = 0
                    sabjil = False
                    maps[nr][nc] += a
t = int(input())
for tc in range(1, t+1):
    n, K = map(int, input().split())
    maps = [list(map(int, input().split()))for _ in range(n)]
    maxh = 0
    maxlist = []
    for i in range(n):
        for j in range(n):
            if maxh < maps[i][j]:
                maxh = maps[i][j]
    maxlen = 0
    for i in range(n):
        for j in range(n):
            if maps[i][j] == maxh:
                visited = [[0] * n for _ in range(n)]
                visited[i][j] = 1
                sabjil = False
                find_road(i,j,1)
    print(f'#{tc} {maxlen}')
