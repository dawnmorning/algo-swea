import sys
sys.stdin = open('5189.txt')
#
# def dfs(idx,s):
#     global minV
#     if 0 not in visited:
#         if s < minV:
#             minV = s
#         return
#     if minV < s:
#         return
#     for i in range(n):
#         if idx == i:
#             continue
#         if visited[i]:
#             continue
#         if i == 0 and 0 in visited[1:]:
#             continue
#         visited[i] = 1
#         dfs(i, s + office[idx][i])
#         visited[i] = 0
#
#
# t = int(input())
# for tc in range(1, t+1):
#     n = int(input())
#     office = [list(map(int, input().split()))for _ in range(n)]
#     minV = 100 ** n
#     visited = [0] * n
#     dfs(0,0)
#     print(f"#{tc} {minV}")

def move(i, k, r):
    global min_total
    if i == r:
        total = 0
        p.append(1)
        for idx in range(N):
            row = p[idx]
            col = p[idx+1]
            total += data[row-1][col-1]
        if total <= min_total:
            min_total = total
    else:
        for j in range(k):
            if used[j] == 0:
                used[j] = 1
                p[i] = a[j]
                move(i+1, k, r)
                used[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    a = [i for i in range(1, N+1)]
    used = [0] * N
    used[0] = 1
    p = [0] * N
    p[0] = 1
    min_total = 999999
    move(1, N, N)
    print(f'#{tc} {min_total}')
