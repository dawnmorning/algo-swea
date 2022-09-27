# import sys
# sys.stdin = open('input (1).txt')
# t = 10
# for tc in range(1, t+1):
#     a = int(input())
#     value = [list(map(int, input().split()))for _ in range(100)]
#     for i in range(100):
#         sumR = 0
#         sumC = 0
#         for j in range(100):
#             sumR += value[i][j]
#             sumC += value[j][i]
#         if sumR < value[i][j]:
#                 sumR = value[i][j]
#         if sumC < value[j][i]:
#                 sumC = value[j][i]


# import sys
# sys.stdin = open('input (1).txt')
n = input()
numbers = []
for _ in range(100):
    numbers.append(list(map(int, input().split())))#100개의 원소를 가지는 리스트
    #가로합 / 세로합/ 대각선합/ 대각선 거꾸로 합 이중에서 가장 큰 거 구하기
    max_value = 0
    #여기 들어가면 전체 i j 합을 구해옴
    for i in range(100):
        my_total = 0 #한 라인이 끝날 시에 my_total을 초기화
        for j in range(100):
            my_total += numbers[i][j]
        if max_value < my_total:
            max_value = my_total
    for i in range(100):
        my_total = 0
        for j in range(100):
            my_total += numbers[j][i]
        if max_value < my_total:
            max_value = my_total
    my_total = 0
    for i in range(100):
        my_total += numbers[i][i]
    if max_value < my_total:
        max_value = my_total
    for i in range(100):
        for j in range(100):
            max_value += numbers[i][99-i]
        if max_value < my_total:
            max_value = my_total
    print(f'#{n} {max_value}')



