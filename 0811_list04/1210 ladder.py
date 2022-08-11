import sys
sys.stdin = open('1210 ladder.txt')
t = 10
for tc in range(1,t+1):
    garbage = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        if arr[99][i] == 2:
            y = i
    x = 98
    while x > 0:
        if y>0 and arr[x][y-1] == 1:
            arr[x][y] = 0
            x -=1
        if y < 99 and arr[x][y + 1] == 1:
            arr[x][y] = 0
            y += 1
        elif arr[x - 1][y] == 1:  # 좌우 길 없고 위로 이동 가능하면 이동
            x -= 1

    print(f'#{tc} {y}')

