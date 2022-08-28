import sys
sys.stdin = open('1208.txt')
t = 10
# for tc in range(1, t+1):
#     dump = int(input())
#     box = list(map(int, input().split()))
#     while dump != 0:
#         for i in range(99,-1,-1):
#             for j in range(i):
#                 if box[j] > box[j+1]:
#                     box[j], box[j+1] = box[j+1], box[j]
#         box[99] = box[99] - 1
#         box[0] = box[0] + 1
#         dump -= 1
#     for i in range(99, -1, -1):
#         for j in range(i):
#             if box[j] > box[j + 1]:
#                 box[j], box[j + 1] = box[j + 1], box[j]
#     print(f'#{tc} {box[99]- box[0]}')
for tc in range(1, t+1):
    dump = int(input())
    box = list(map(int, input().split()))
    while dump != 0:
        box.sort()
        box[99] -= 1
        box[0] += 1
        dump -= 1
    box.sort()
    print(f'#{tc} {box[-1] - box[0]}')
