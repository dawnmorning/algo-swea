# import sys
# sys.stdin = open('1210 ladder.txt')
# t = 10
# for tc in range(1,t+1):
#     garbage = int(input())
#     arr = [list(map(int, input().split())) for _ in range(100)]
#     for i in range(100):
#         if arr[99][i] == 2:
#             x = i
#     y = 98
#     while y > 0:
#         if x>0 and arr[y][x-1] == 1:
#             arr[y][x] = 0
#             x -= 1
#         if x< 99 and arr[y][x+1] == 1:
#             arr[y][x] = 0
#             x += 1
#         if arr[y-1][x] == 1:
#             y -= 1
#     print(f'#{tc} {x}')

#교수님 ver

import sys
sys.stdin = open('1210 ladder.txt')
for _ in range(10):
    tc = input()
    # 사다리의 2차원 배열을 받아올 필요가 있음
    matrix = [list(map(int, input().split())) for _ in range(100)]
    #당첨된 곳을 찾고 역순으로 올라가서 x를 찾는다!
    for col_x in range(100):
        if matrix[99][col_x] == 2:
            col = col_x
    #좌, 우, 위 델타
    dr = [0,0,-1]
    dc = [-1,1,0]

    row = 99
    while row != 0: #가장 윗부분에 도착
        #방향탐색 (세 방향) 위에 적은 좌 우 위
        for idx in range(3):
            next_row = row + dr[idx]
            next_col = col + dc[idx]
            if 0 <= next_row < 100 and 0 <= next_col < 100:
                if matrix[next_row][next_col] == 1:
                    matrix[row][col] = 0 #있던 자리를 0으로 만들고
                    row = next_row  # 갱신되면서 이동
                    col = next_col
    print(f'#{tc} {col}')





