import sys
sys.stdin = open('4871.txt')
t = int(input())

def findload(v):
    #1. 현재 정점 방문!!!!
    visited[v] = 1
    result.append(v) #현재 방문한 곳 추가
    # 0으로 된 갈 곳이 있는지,
    for nxt in adjlist[v]:
        if visited[nxt] == 0:
            findload(nxt)

for tc in range(1, t+1):
    V, E = map(int, input().split())
    adjlist = [[] for _ in range(V+1)]  # 정보 담을 공간
    visited = [0] * (V+1)  #방문한 곳 기록 하기
    result = []
    for i in range(E):
        frm, to = map(int, input().split())
        adjlist[frm].append(to)
    S, G = map(int, input().split())
    findload(S)
    value = G in result
    print(f'#{tc} {int(value)}')
    # 정보 담을 공간 필요
    # 인접리스트 만들 공간 필요
    # 방문하고 기록남길 리스트필요
