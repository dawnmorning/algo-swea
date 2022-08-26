import sys
sys.stdin = open('4861.txt')
t = int(input())
for tc in range(1, t+1):
    n, m  = map(int, input().split())
    arr = [list(input())for _ in range(n)]
    for i in range(n):
        for j in range(n-m+1):
            row = []
            col = []
            for k in range(m):
                row += arr[i][j+k]
                col += arr[j+k][i]
            if row == row[::-1]:
                last = ''.join(row)
            if col == col[::-1]:
                last = ''.join(col)
    print(f'#{tc} {last}')