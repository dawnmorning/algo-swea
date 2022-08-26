import sys
sys.stdin = open('1961.txt')

T = int(input())

def rotate(arr):   # 배열을 왼쪽 하단부터 세로로 읽는 함수 = 90도 회전하는 함수
    num = ''       # 회전시킨 배열의 각 행을 str으로 생성
    arr_ro = []
    for i in range(N):
        for j in range(N - 1, -1, -1):
            num += arr[j][i]
        arr_ro.append(num)
        num = ''
    return arr_ro

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]

    arr_90 = rotate(arr)
    arr_180 = rotate(arr_90)
    arr_270 = rotate(arr_180)

    print(f'#{tc}')
    for i in range(N):
        for a in [arr_90, arr_180, arr_270]:    # 각 배열의 i번째 str을 출력
            print(f'{a[i]} ', end='')
        print()