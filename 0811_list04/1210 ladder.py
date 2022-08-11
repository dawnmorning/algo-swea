import sys
sys.stdin = open('1210 ladder.txt')
t = 10
for tc in range(1,t+1):
    garbage = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        if arr[99][i] == 2:
            x = i
    y = 98
    while y > 0:
        if x>0 and arr[y][x-1] == 1:
            arr[y][x] = 0
            x -= 1
        if x< 99 and arr[y][x+1] == 1:
            arr[y][x] = 0
            x += 1
        if arr[y-1][x] == 1:
            y -= 1
    print(f'#{tc} {x}')




