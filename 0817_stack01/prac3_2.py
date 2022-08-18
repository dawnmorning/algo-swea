# def dfs(v, N):
#     visited = [0] * N  # visited 생성
#     stack = [0] * N  # stack 생성
#     top = -1
#     visited[v] = 1  # 시작점 방문 표시
#     print(v)
#     while True:
#         for w in adjlist[v]:  # if ( v의 인접 정점 중 방문 안 한 정점 w가 있으면)
#             if visited[w] == 0:   #visited 인덱스가 비어있으면,
#                 top += 1  # v <- w 스택을 쌓고,
#                 stack[top] = v #스택의 인덱스에 쌓자!
#                 v = w  # w에 방문
#                 print(v)  # 방문
#                 visited[w] = 1  # visited[w] <- true
#                 break
#         else:  # w가 없으면
#             if top != -1:  # 스택이 비어있지 않은 경우
#                 v = stack[top]  # pop
#                 top -= 1
#             else:
#                 break
# V, E = map(int,input().split())
# N = V + 1
# adjlist = [[]for _ in range(N)]
# for _ in range(E):
#     a, b = map(int, input().split())
#     adjlist[a].append(b)
#     adjlist[b].append(a)    #갈 수 있는 인접 정점을 만들어 주는 것
#
# dfs(1, N)


import sys
sys.stdin = open('prac3.txt')
V = 7 # 정점의 개수
#모든 경로를 받기
edge_list = list(map(int, input().split(', ')))
E = len(edge_list)//2 #간선의 개수

#인접 정점 (인접행렬로 만들기) 이차원배열로 나타내기
# graph = ([0] * (V+1)) * (V+1)  #0번을 안 쓰기 위해 V+1
graph = [[0] * (V+1) for _ in range(V+1)]
for idx in range(E):
    #graph[시작점][끝점] = 1
    #graph[끝점][시작점] = 1
    frm = edge_list[idx*2] #시작점 edge_list의 짝수번째
    to = edge_list[idx*2 + 1] #끝점
    graph[frm][to] = 1
    graph[to][frm] = 1

visited = [False] * (V + 1)
now = 1
result = [now]
stack = [now] #방문했던 경로 저장
while stack:   #stack이 있는동안 반복
    # 1. 방문한다.
    visited[now] = 1
    # 2. 인접 정점을 확인한다. (0번 빼니까 V+1)
    for nxt in range(V+1):
    # 3. 인접 정점을 이미 방문했는지 확인한다.
        if graph[now][nxt] == 1 and visited[nxt] == 0: #연결된 곳이고 방문하지 않았다면
    # 4. 이동한다.
    # 4-1. 이전 경로를 stack 넣는다
            stack.append(now)
    # 4-2. 방문 정점을 변경한다.
            now = nxt
            result.append(nxt)
            break  #해당 for문을 멈춤
    else: #모든 정점이 방문되었다면 stack에서 pop
        now = stack.pop()
print('-'.join(map(str,result)))