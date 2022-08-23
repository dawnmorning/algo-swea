import sys
sys.stdin = open('4881.txt')

# def find_minsum(num, finding):
#     global min_sum
#     if min_sum < finding:
#         return
#     if num == n:
#         if min_sum > finding:
#             min_sum = finding
#     for i in range(n):
#         if check[i] != 0 :
#             check[i] = 1
#             find_minsum(num+1, finding + arr[num][i])
#             check[i] = 0
#
# t = int(input())
# for tc in range(1, t+1):
#     n = int(input())
#     arr = [list(map(int, input().split()))for _ in range(n)]
#     check = [0] * n
#     min_sum = 123456789
#     find_minsum(0,0)
#     print(f'#{tc} {min_sum}')

def per(k,midV):
    global minV
    if minV < midV:
        return
    if k == N:
        if minV > midV:
            miV = midV
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            per(k+1, midV+arr[k][i])
            visited[i] = False
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split()))for _ in range(N)]
    minV = 1000000
    visited = [False] * N
    per(0,0)
    print(f'#{tc} {minV}')


