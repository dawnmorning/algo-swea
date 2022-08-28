import sys
sys.stdin = open('2805.txt')
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    farm = [list(map(int, input()))for _ in range(n)]
    mid = n // 2
    result = 0
    for i in range(mid+1):
        for j in range(mid-i,mid+i+1):
            result += farm[i][j] + farm[n-i-1][j]
    print(f'#{tc} {result - sum(farm[mid])}')
