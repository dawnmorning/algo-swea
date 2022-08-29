import sys
sys.stdin = open('9489.txt')
t = int(input())
for tc in range(1, t+1):
    n, m = map(int,input().split())
    place = [list(map(int, input().split()))for _ in range(n)]
    max_cnt = 0
    for i in range(n):
        cnt = 0
        for j in range(m):
            if place[i][j] == 1:
                cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
            else:
                cnt = 0
    for i in range(m):
        cnt = 0
        for j in range(n):
            if place[j][i] == 1:
                cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
            else:
                cnt = 0
    print(f'#{tc} {max_cnt}')


