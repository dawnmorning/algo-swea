import sys
sys.stdin = open('2805.txt')
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]

    mid = n // 2  # 중점 부터 좌우로 한칸씩 늘어남
    answer = 0
    for i in range(mid + 1):  # 위아래가 대칭이므로 절반까지만 구한다.
        for j in range(mid - i, mid + i + 1):  # 중심을 기준으로 왼쪽으로 1칸, 오른쪽으로 1칸 범위를 늘려 나간다.
            answer += farm[i][j] + farm[n - i - 1][j]    #중간 기준 위 아래 인덱스 값

    print(f'#{tc} {answer - sum(farm[mid])}')
