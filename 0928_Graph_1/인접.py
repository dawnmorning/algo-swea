'''
6 8
0 1 0 2 0 5 0 6 3 4 3 5 6 4 5 4
'''
v, e = map(int, input().split())  # 마지막 정점 번호, 간선 개수
arr = list(map(int, input().split()))
# 인접행렬
adjM = [[0] * (v+1) for _ in range(v+1)] # 인접행렬
adjList = [[] for _ in range(v+1)]
for i in range(e):
    n1, n2 = arr[2 * i], arr[2*i + 1]
    adjM[n1][n2] = 1
    adjM[n2][n1] = 1   # 방향이 없는 경우 추가

    adjList[n1].append(n2)
    adjList[n2].append(n1)