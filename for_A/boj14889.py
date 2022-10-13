import sys
input = sys.stdin.readline

def dfs(depth, idx):
    global minV,n
    if depth == n//2:
        t1 = t2 = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j] :
                    t1 += company[i][j]
                elif not visited[i] and not visited[j]:
                    t2 += company[i][j]
        minV = min(minV, abs(t1-t2))

        return


    for i in range(idx,n):
        if visited[i]:
            continue
        if not visited[i]:
            visited[i] = 1
            dfs(depth+1, i+1)
            visited[i] = 0

n = int(input())
company = [list(map(int, input().split())) for _ in range(n)]
minV = 20000
visited = [0] * n
dfs(0,0)
print(minV)