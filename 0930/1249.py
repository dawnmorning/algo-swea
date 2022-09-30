import sys
sys.stdin = open('1249.txt')
from collections import deque
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    supply = [list(map(int, list(input())))for _ in range(n)]
    time = [[1234567890] * n for _ in range(n)]
    time[0][0] = 0
    q = deque([(0,0)])
    # q.append((0,0))
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    while q:
        r,c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if time[nr][nc] > time[r][c] + supply[nr][nc]:
                    time[nr][nc] = time[r][c] + supply[nr][nc]
                    q.append((nr,nc))
    print(f'#{tc} {time[-1][-1]}')
