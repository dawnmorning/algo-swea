import sys
sys.stdin = open('5251.txt', 'r')


def digkstra():
    while Q:
        now, cost = Q.pop(0)   # 정점 정보와 거리

        if D[now] < cost:      # 주어진 거리보다 저장된 거리가 더 작으면 skip
            continue

        visited[now] = True
        # 현재 정점의 인접 정점을 선택하여 그 인접 정점을 확인
        for v in range(len(adj_list[now])):
            n_v, n_cost = adj_list[now][v]   # 연결된 정점과 그 거리
            if not visited[n_v]:
                # 현재까지의 거리와 연결된 정점의 거리를 더한 값이
                # 저장된 값보다 작다면 갱신
                if cost + n_cost < D[n_v]:
                    D[n_v] = cost + n_cost
                    Q.append((n_v, D[n_v]))   # 다음 정점과 갱신된 거리를 Queue에 등록


t = int(input())
for tc in range(1, t+1):
    INF = 1000000
    V, E = map(int, input().split())
    # 인접 리스트
    adj_list = [[] for _ in range(V+1)]

    for _ in range(E):
        s, v, d = map(int, input().split())
        adj_list[s].append((v, d))


    D = [INF] * (V+1)
    D[0] = 0
    for v, d in adj_list[0]:   # 시작 정점에서 인접한 정점 거리 저장
        D[v] = d


    visited = [False] * (V+1)
    visited[0] = True

    Q = [*adj_list[0]]  # Queue 에 시작점으로 부터 이어진 값을 넣는다.
    digkstra()
    print(f'#{tc} {D[-1]}')