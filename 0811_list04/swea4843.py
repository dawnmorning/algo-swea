# import sys
# from collections import deque
# sys.stdin = open('4843.txt')
# T = int(input())
# for tc in range(1,T+1):
#     n = int(input())
#     num = list(map(int,input().split()))
#     standard = n//2
#     li_1=[]
#     li_2=[]
#     for i in range(len(num)-1,0,-1):
#         for j in range(i):
#             if num[j] > num[j+1]:
#                 num[j+1], num[j] = num[j], num[j+1]
#     li_1.append(num[n:standard - 1:-1])
#     li_2.append(num[:standard])
#     for a in li_1:
#         real_1 = a
#     for b in li_2:
#         real_2 = b
#     q1 = deque(a)
#     q2 = deque(b)
#     li = 0
#     for k in range(n):
#         if k % 2 == 0:
#             li += q1.popleft()
#         else:
#             li += q2.popleft()
#         print(li, end= ' ')
#     print(f'#{tc} {li}')


# import sys
# sys.stdin = open('4843.txt')
#
# def selectionSort(a, N):
#     for i in range(N-1):
#         minIdx = i
#         for j in range(i+1, N):
#             if a[minIdx] > a[j]:
#                 minIdx = j
#         a[i], a[minIdx] = a[minIdx], a[i]
#
#     return a
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     value = list(map(int, input().split()))
#     sorted_value = selectionSort(value, len(value))
#
#     print(f'#{tc}', end=' ')
#     for j in range(10):
#         res = 0
#         if j % 2:
#             res += sorted_value.pop(0)
#         else:
#             res += sorted_value.pop()
#         print(res, end=' ')
#     print()

import sys
sys.stdin = open('4843.txt')
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    num = list(map(int,input().split()))
    standard = n//2
    li_1=[]
    li_2=[]
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            if num[j] > num[j+1]:
                num[j+1], num[j] = num[j], num[j+1]
    li_1.append(num[n:standard - 1:-1])
    li_2.append(num[:standard])
    for a in li_1:
        real_1 = a
    for b in li_2:
        real_2 = b
    print(f'#{tc}', end = ' ')
    for k in range(10):
        li = 0
        if k % 2 == 0:
            li += a.pop(0)
        else:
            li += b.pop(0)
        print(f'{li}', end=' ')
    print()

# *li 하면 리스트 벗겨져서 나옴