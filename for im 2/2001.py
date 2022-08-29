import sys
sys.stdin = open('2001.txt')
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    fly = [list(map(int, input().split()))for _ in range(n)]
    max_death = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            death = 0
            for k in range(m):
                for l in range(m):
                    death = death + fly[i+k][j+l]
                    if max_death < death:
                        max_death = death
    print(f'#{tc} {max_death}')
