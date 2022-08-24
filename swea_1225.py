# import sys
# sys.stdin = open('1225.txt')
# t = 10
# for tc in range(1, t+1):
#     waste = int(input())
#     number = list(map(int,input().split()))
#     i = 1
#     while number[-1] != 0:
#         if i == 6:
#             i = 1
#         first = number.pop(0) - i
#
#         if first <= 0:
#             first = 0
#
#         number.append(first)
#         i += 1
#     print(f'#{tc}', *number)

import sys
sys.stdin = open('1225.txt')
t = 10
for tc in range(1, t+1):
    waste = int(input())
    number = list(map(int,input().split()))
    while number[-1] != 0:
        for i in range(1,6):
            first = number.pop(0) - i

            if first <= 0:
                number.append(0)
                break
            else:
                number.append(first)
    print(f'#{tc}', *number)