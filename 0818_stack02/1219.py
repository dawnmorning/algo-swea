import sys
sys.stdin = open('1219.txt')
def findload(v):
    visited[v] = 1
    result.append(v)
    for i in adjlist[v]:
        if visited[i] == 0:
            findload(i)
for _ in range(10):
    t, e = map(int,input().split())
    adjlist = [[] for _ in range(100)]
    visited = [0] * 100
    road = list(map(int,input().split()))
    result = []
    for i in range(e):
        frm, to = road[2*i], road[(2*i) + 1]
        adjlist[frm].append(to)
    findload(0)
    value = 99 in result
    print(f'#{t} {int(value)}')
