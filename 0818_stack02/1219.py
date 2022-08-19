# import sys
# sys.stdin = open('1219.txt')
# def findload(v):
#     visited[v] = 1
#     result.append(v)
#     for i in adjlist[v]:
#         if visited[i] == 0:
#             findload(i)
# for _ in range(10):
#     t, e = map(int,input().split())
#     adjlist = [[] for _ in range(100)]
#     visited = [0] * 100
#     road = list(map(int,input().split()))
#     result = []
#     for i in range(e):
#         frm, to = road[2*i], road[(2*i) + 1]
#         adjlist[frm].append(to)
#     findload(0)
#     value = 99 in result
#     print(f'#{t} {int(value)}')

#길이 존재하는지를 물음.
#최대 2개의 갈림길이 존재, 모든 길은 일방 통행. 방향은 단방향
import sys
sys.stdin = open('1219.txt')
t = 10
for _ in range(1, t+1):
    tc, E = map(int,input().split()) #테스트 케이스, 간선의 개수
    graph = [[] for _ in range(100)]
    V = list(map(int,input().split()))
    #인접 리스트
    for idx in range(0, len(V), 2):
        frm = V[idx]
        to = V[idx +1]
        graph[frm].append(to) #단방향이기에 하나만
    start = 0 #시작 정점
    visited = [False for _ in range(100)]
    stack = [start]
    now = start #현재 위치
    while stack: #스택이 비어있지 않는 동안,
        visited[now] = 1  #방문처리
        #인접 정점 찾기
        for nxt in graph[now]:
            # if nxt == 99
            #     flag
            #     break
            if visited[nxt] == 0:   #if not visited[nxt]:
                stack.append(now)
                now = nxt
                break
        else:
            now = stack.pop()
    print(f'#{tc} {int(visited[99])}')