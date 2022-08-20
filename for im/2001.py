import sys
sys.stdin = open('2001.txt')
t = int(input())
for tc in range(1, t+1):
    n, m = map(int,input().split())
    box = [list(map(int,input().split()))for _ in range(n)]
    max_cnt = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            cnt = 0
            for k in range(m):
                for l in range(m):
                    number = box[k+i][l+j]
                    cnt += number
            if max_cnt<cnt:
                max_cnt = cnt
    print(f'#{tc} {max_cnt}')


