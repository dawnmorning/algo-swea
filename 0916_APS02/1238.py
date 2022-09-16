#1.
import sys
sys.stdin = open('1238.txt')
t = 10
for tc in range(1, t+1):
    length, start = map(int, input().split())
    adjlist = [[] for _ in range(101)]
    visited = [0 for _ in range(101)]

    contact = list(map(int, input().split()))
    for i in range(0,length,2):
        adjlist[contact[i]].append(contact[i+1])
    q = []
    q.append(start)
    visited[start] = 1
    while q:
        v = q.pop(0)
        for vv in adjlist[v]:
            if visited[vv] == 0:
                visited[vv] = visited[v] + 1
                q.append(vv)
    v_max = 0
    for i in range(101):
        if visited[i] >= visited[v_max]:
            v_max = i
    print(f'#{tc} {v_max}')
