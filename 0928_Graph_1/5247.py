import sys
sys.stdin = open('5247.txt')
from collections import deque
def bfs(s):
    global m
    q = deque([s])
    visited = [0] * 1000001
    visited[s] = 0
    while q:
        s = q.popleft()
        for i in [s+1, s-1, s*2, s-10]:
            if i < 1 or i > 1000000:
                continue
            if i == m:
                return visited[s] + 1
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[s] + 1

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    res = bfs(n)
    print(f'#{tc} {res}')