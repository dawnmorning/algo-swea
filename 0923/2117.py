import sys
sys.stdin = open('2117.txt')
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    info = [list(map(int,input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            for k in range(1, 2 * n):
                temp = 0
                cost = k * k + (k - 1) * (k - 1)
                for r in range(n):
                    for c in range(n):
                        if abs(i-r) + abs(j-c) < k:  # 전체 범위중 마름모의 변 길이 만큼 탐색하는데, 그 범위 안에 들어가 있으면 그 집은 가능하므로 더해주기
                            temp += info[r][c]
                TotalRevenue = temp * m - cost
                if TotalRevenue >= 0 and cnt < temp:   # 케이스 43개만 맞으시는 분들은, 총 수입이 0인 경우도 통과가능함을 고려하셔야 합니다. 수익이 없다 = 손해도 없다 = 0도 가능하다.
                    cnt = temp
    print(f'#{tc} {cnt}')