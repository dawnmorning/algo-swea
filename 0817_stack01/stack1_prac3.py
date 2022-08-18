def dfs(v, N):
    visited = [0] * N  # visited 생성
    stack = [0] * N  # stack 생성
    top = -1
    visited[v] = 1  # 시작점 방문 표시
    print(v)
    while True:
        for w in adjlist[v]:  # if ( v의 인접 정점 중 방문 안 한 정점 w가 있으면)
            if visited[w] == 0:
                top += 1  # v <- w
                stack[top] = v
                v = w  # w에 방문
                print(v)  # 방문
                visited[w] = 1  # visited[w] <- true
                break
        else:  # w가 없으면
            if top != -1:  # 스택이 비어있지 않은 경우
                v = stack[top]  # pop
                top -= 1
            else:
                break
V, E = map(int,input().split())
N = V + 1
adjlist = [[]for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjlist[a].append(b)
    adjlist[b].append(a)

dfs(1, N)
