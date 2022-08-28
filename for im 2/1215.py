import sys
sys.stdin = open('1215.txt')
t = 10
for tc in range(1, t+1):
    n = int(input())
    arr = [list(input())for _ in range(8)]
    cnt = 0
    for i in range(8):
        for j in range(8-n+1):
            if arr[i][j:j+n] == arr[i][j:j+n][::-1]:
                cnt += 1
    for r in range(8):
        for c in range(8):
            if r>c:
                arr[c][r], arr[r][c] = arr[r][c], arr[c][r]
    for i in range(8):
        for j in range(8 - n + 1):
            if arr[i][j:j + n] == arr[i][j:j + n][::-1]:
                cnt += 1
    print(f'#{tc} {cnt}')