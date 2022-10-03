import sys
sys.stdin = open('5251.txt')

def dijkstra():
    q = [*adjlist[0]]
    while q:
        now, cost = q.pop(0)
        visited[now] = 1

        if d[now] < cost:
            continue

        for i in range(len(adjlist[now])):
            next_i, next_cost = adjlist[now][i]
            if visited[next_i] == 0:
                if cost+next_cost < d[next_i]:
                    d[next_i] = cost+next_cost
                    q.append((next_i, d[next_i]))



t = int(input())
for tc in range(1,t+1):
    N,E = map(int, input().split())
    adjlist = [[] for _ in range(N+1)]
    inf = 9876543210
    d = [inf] * (N+1)
    d[0] = 0
    visited = [0] * (N+1)
    visited[0] = 0
    for i in range(E):
        s,e,w = list(map(int, input().split()))
        adjlist[s].append((e,w))
    for e,w in adjlist[0]:
        d[e] = w

    dijkstra()
    print(f'#{tc} {d[-1]}')