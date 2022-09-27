import sys
sys.stdin = open('5209.txt')
def dfs(s,c):
    global min_c
    if s == n:
        if c < min_c:
            min_c = c
        return

    elif c >= min_c:
        return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(s + 1, c + cost[s][i])
            visited[i] = 0


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    cost = [list(map(int, input().split()))for _ in range(n)]
    min_c = 99 ** 15
    visited = [0] * n
    dfs(0,0)
    print(f'#{tc} {min_c}')

