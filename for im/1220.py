# import sys
# sys.stdin = open('1220.txt')
#
# t = 10
# for tc in range(1, t+1):
#     n = int(input())
#     magnet = [list(map(int, input().split()))for _ in range(n)]
#     cnt = 0
#     for i in range(n):
#         meet = []
#         for j in range(n):
#             if not meet and magnet[j][i] == 1:
#                 meet.append(1)
#             if meet and  magnet[j][i] == 2 :
#                 cnt = cnt + meet.pop()
#     print(f'#{tc} {cnt}')

# import sys
# sys.stdin = open('1220.txt')
# t = 10
# for tc in range(1, t+1):
#     n = int(input())
#     magnet = [list(map(int, input().split()))for _ in range(n)]
#     cnt = 0
#     for i in range(n):
#         value = []
#         for j in range(n):
#             if magnet[j][i] == 1 and not value:
#                 value.append(1)
#             if magnet[j][i] == 2 and 1 in value:
#                 value.pop()
#                 cnt += 1
#     print(f'#{tc} {cnt}')

import sys
sys.stdin = open('1220.txt')
t = 10
for tc in range(1, t+1):
    n = int(input())
    magnet = [list(map(int, input().split()))for _ in range(n)]
    cnt = 0
    for i in range(n):
        stack = []
        for j in range(n):
            if magnet[j][i] == 1 and not stack:
                stack.append(magnet[j][i])
            if magnet[j][i] == 2 and 1 in stack:
                stack.pop()
                cnt +=1
    print(f'#{tc} {cnt}')


















