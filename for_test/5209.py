import sys
sys.stdin = open('5209.txt')
def find_cost(idx, value):
    global minV
    if idx == n:
        minV = min(minV, value)

    elif value >= minV:
        return
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            find_cost(idx+1, value + factory[idx][i])
            visited[i] = 0



t = int(input())
for tc in range(1, t+1):
    n = int(input())
    factory = [list(map(int, input().split()))for _ in range(n)]
    minV = 9876543210
    visited = [0] * n
    find_cost(0,0)
    print(f'#{tc} {minV}')