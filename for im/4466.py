import sys
sys.stdin = open('4466.txt')
t = int(input())
for tc in range(1, t+1):
    n, k = map(int,input().split())
    score = list(map(int,input().split()))
    value = 0
    # for i in range(n-k+1):
    #     pre_value = 0
    #     for j in range(k):
    #         pre_value = sum(score[i:k])
    #         if value < pre_value:
    #             value = pre_value
    # print(f'#{tc} {value}')
    score.sort(reverse = True)
    for i in range(k):
        value += score[i]
    print(f'#{tc} {value}')