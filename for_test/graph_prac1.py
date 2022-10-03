def dfs(s):
    print(s, end = ' ')
    visited[s] = 1
    for i in adjlist[s]:
        if not visited[i]:
            dfs(i)

def bfs(s):
    q = []
    q.append(s)
    visited_bfs[s] = 1
    while q:
        v = q.pop(0)
        print(v, end = ' ')
        for i in adjlist[v]:
            if visited_bfs[i] == 0:
                visited_bfs[i] = 1
                q.append(i)

v = 7
e = 8
adjlist = [[] for _ in range(v+1)]
info = list(map(int, input().split()))
visited = [0] * (v+1)
visited_bfs = [0] * (v+1)
for i in range(e):
    a,b = info[2*i], info[2*i +1]
    adjlist[a].append(b)
    adjlist[b].append(a)
dfs(1)
print()
bfs(1)