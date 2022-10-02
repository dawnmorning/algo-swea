import sys
sys.stdin = open('5189.txt')

def dfs(idx,start,total):
    global minV
    if idx == n-1:
        minV = min(minV, cost[start][0] + total)
        return

    for i in range(1,n):
        if visited[i] == 0 and start != i:
            visited[i] = 1
            dfs(idx + 1, i, total + cost[start][i])
            visited[i] = 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    cost = [list(map(int, input().split())) for _ in range(n)]
    minV = 100 ** n
    visited = [0] * n
    dfs(0,0,0)
    print(f'#{tc} {minV}')

