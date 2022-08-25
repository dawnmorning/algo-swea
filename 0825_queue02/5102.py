import sys
sys.stdin = open('5102.txt')
def bfs(s,g,n):
    visited = [0 for _ in range(n+1)]
    visited[s] = 1
    q = []
    q.append(s)
    while q:
        v = q.pop(0)
        if s == g:
            return visited[v] - 1
        for w in adjlist[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1
    return 0



t = int(input())
for tc in range(1, t+1):
    v ,e = map(int,input().split())
    n = v+1
    adjlist = [[] for _ in range(n)]
    for _ in range(e):
        a,b = map(int,input().split())
        adjlist[a].append(b)
        adjlist[b].append[a]
    s, g= map(int, input().split())
    print(f'#{tc} {bfs(s,g,v)}')
