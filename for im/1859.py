import sys
sys.stdin = open('1859.txt')
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    price = list(map(int, input().split()))
    #앞에서 부터 계산

    # result = 0
    # restart = 0
    # while restart < n:
    #     maxidx = restart
    #     for i in range(restart, n):
    #         if price[maxidx] < price[i]:
    #             maxidx = i
    #
    #     sumV = 0
    #     for i in range(restart, maxidx):
    #         sumV += price[i]
    #     result += (maxidx-restart) * price[maxidx] - sumV
    #     restart = maxidx + 1
    # print(f'#{tc} {result}')

    #뒤에서부터 계산
    result = 0
    maxV = price[n-1]
    for idx in range(n-2,-1,-1):
        if price[idx] > maxV:
            maxV = price[idx]
        else:
            result += maxV - price[idx]
    print(f'#{tc} {result}')


