def dfs(v):
    print(v)
    visited[v] = 1
    for w in adjlist[v]:
        if visited[w] == 0:
            dfs(w)


V, E = map(int, input().split())
n = V + 1
adjlist = [[] for _ in range(n)]
for _ in range(E):
    a, b = map(int, input().split())
    adjlist[a].append(b)
    adjlist[b].append(a)
visited = [0] * n  # visited 생성
dfs(0)