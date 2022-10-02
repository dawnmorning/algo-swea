import sys
input = sys.stdin.readline

def bfs(v):
    visited_bfs[v] = 1
    q = ([v])
    while q:
        a = q.pop(0)
        print(a, end = ' ')
        for i in adjlist[a]:
            if visited_bfs[i] == 0:
                visited_bfs[i] = 1
                q.append(i)

def dfs(v):
    visited_dfs[v] = 1
    print(v, end = ' ')
    for i in adjlist[v]:
        if visited_dfs[i] == 0:
            dfs(i)

n,m,v = map(int, input().split())
adjlist = [[] for _ in range(n+1)]
for _  in range(m):
    a, b = map(int, input().split())
    adjlist[a].append(b)
    adjlist[b].append(a)

visited_dfs = [0] * (n+1)
dfs(v)
print()
visited_bfs = [0] * (n+1)
bfs(v)