import sys
sys.stdin = open('2001.txt')
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    wing = [list(input().split())for _ in range(n)]
    max_value = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            num = 0
            for k in range(m):
                for l in range(m):
                    now = wing[i+k][j+l]
                    num += int(now)
            if max_value < num:
                max_value = num
    print(f'#{tc} {max_value}')

