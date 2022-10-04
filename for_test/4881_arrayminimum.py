import sys
sys.stdin = open('4881.txt')

def dfs(idx,cost):
    global mini

    if mini <= cost:
        return

    if idx == n:
        mini = min(mini, cost)
        return
    for i in range(n):
        if not v[i]:
            v[i] = 1
            dfs(idx+1, cost + arr[idx][i])
            v[i] = 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    v = [0] * (n+1)
    mini = 10000
    dfs(0,0)
    print(f'#{tc} {mini}')