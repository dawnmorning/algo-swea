import sys
sys.stdin = open('5251.txt')

def van_dijk():
    while q:
        now, cost = q.pop(0)

        if d[now] < cost:
            continue

        for i in range(len(adjlist[now])):
            next_i, next_cost = adjlist[now][i]
            if cost + next_cost < d[next_i]:
                d[next_i] = cost + next_cost
                q.append((next_i, d[next_i]))


t = int(input())
for tc in range(1, t+1):
    V, E = map(int, input().split())
    adjlist = [[] for _ in range(V+1)]
    infinity = 1000000
    for _ in range(E):
        s,e,w, = map(int,input().split())
        adjlist[s].append((e,w))
    d = [infinity] * (V+1)
    d[0] = 0
    for e,w in adjlist[0] :
        d[e] = w

    q = [*adjlist[0]]
    van_dijk()
    print(f'#{tc} {d[-1]}')