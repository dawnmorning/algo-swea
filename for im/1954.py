import sys
sys.stdin = open('1954.txt')
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    x = -1
    y = 0
    arr = [[0] * n for _ in range(n)]
    arr[0][0] = 1
    num = 2
    for j in range(1,n):
        arr[0][j] = num
        num += 1
    while n > 0:
        n -= 1  # 우측과 하단은 채워야 하는 개수가 같다.

        for i in range(n):  # 우측 아래로 한칸찍 내려가며
            y += 1
            arr[y][x] = num
            num += 1

        for i in range(n):  # 하단 왼쪽으로 한칸씩
            x -= 1
            arr[y][x] = num
            num += 1

        n -= 1  # 좌측과 상단의 채워야 하는 개수가 같다.

        for i in range(n):  # 좌측 위로 한칸씩
            y -= 1
            arr[y][x] = num
            num += 1

        for i in range(n):  # 상단 오른쪽으로 한칸씩
            x += 1
            arr[y][x] = num
            num += 1

    print(f'#{tc}')

    n = len(arr)  # N이 0이나 1로 초기화 했으므로

    for i in range(n):
        for j in range(n):
            print(f'{arr[i][j]}', end=' ')
        print()