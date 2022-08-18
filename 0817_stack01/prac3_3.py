import sys
sys.stdin = open('prac3.txt')

def DFS(now):
    # 1. 현재 정점 방문 표시
    visited[now] = 1
    result.append(now) #방문경로 체크
    # 2. 인접 정점 확인
    for nxt in range(V+1):
        if graph[now][nxt] == 1 and visited[nxt] == 0:
    # 3. 이동가능하다면 이동
            DFS(nxt)
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

visited = [False] * (V+1)
result = []
DFS(1)
print(result)
