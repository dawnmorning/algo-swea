import sys
sys.stdin = open('input.txt')
# # number = int(input())
# # res = '홀수' if number % 2 else '짝수'
# # print(f'{res}입니다.')
#
# # 만약에 input 에서 정수가 1개 이상이라면? - 공백으로 구분되어서 입력되어 진다.
# #입력되는 두 수를 더하시오.
# # print(input().split())
#
# # 여러 줄 입력이 있을 때(2차원 리스트로 다룸)
# n = int(input()) #반드시 입력 줄 수가 명시되어 있음 (첫번 째 input은 라인 수를 받는다.)
# li = []
# for _ in range(n):#반복되는 횟수만큼 for 작성 ('_'는 반복되는 숫자가 필요가 없는 경우)
#     li.append(list(map(int, input().split()))) #한줄 씩 계속 불러옴
#
# print(li)
for case in range(1, int(input())+1):
    n = int(input())
    li = list(map(int, input().split()))
    max_value = 0

    for i in range(n):
        cnt = 0
        for j in range(i+1, n):
            if li[i] > li[j]:
                cnt += 1

        if cnt > max_value:
            max_value = cnt

    print(f'#{case} {max_value}')