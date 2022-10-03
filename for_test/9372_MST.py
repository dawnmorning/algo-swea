import sys
input = sys.stdin.readline

from collections import deque
def bfs(s):
    global cnt
    q = deque()
    q.append(s)
    visited[s] = 1
    while q:
        v = q.popleft()
        for i in adjlist[v]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)
                cnt += 1
    return cnt


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    adjlist = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    cnt = 0
    for _ in range(m):
        a,b = map(int, input().split())
        adjlist[a].append(b)
        adjlist[b].append(a)
    bfs(1)
    print(cnt)