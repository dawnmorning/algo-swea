import sys
sys.stdin = open('1767.txt')
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maxynoth = [list(map(int, input().split())) for _ in range(n)]
    core_cnt = 0
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                if maxynoth[i][j] == 1:
                    core_cnt += 1
    