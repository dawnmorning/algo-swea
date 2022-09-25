import sys
sys.stdin = open('5188.txt')

def find_path(row,col):

    if row == n -1 and col == n-1:
        return arr[-1][-1]


    if row >= n or col >= n : # 더 이상 이동할 수 없는 경우
        return 999999999 # 임의의 가장 큰 수

    else:
        res_r = arr[row][col] + find_path(row+1, col)  # 현재 위치 + 아래로 이동한 값
        res_c = arr[row][col] + find_path(row, col + 1) # 현재 위치 + 오른쪽으로 이동한 값
        return res_r if res_r <= res_c else res_c
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    row=col = 0
    res = find_path(row, col)
    print(f'#{tc} {res}')
