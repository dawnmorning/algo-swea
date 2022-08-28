import sys
sys.stdin = open('1211.txt')
t = 10
for tc in range(1, t+1):
    a = input()
    ladder = [list(map(int, input().split()))for _ in range(100)]
    min_count = 100000
    result = 0
    # dr = [1,0,0]
    # dc = [0,-1,1]
    for i in range(100):
        if ladder[0][i] == 1:
            col = i
            cnt = 0
            for j in range(100):
                if col > 0 and ladder[j][col-1] == 1:
                    while col > 0 and ladder[j][col-1] != 0:
                        col -= 1
                        cnt += 1
                elif col < 99 and ladder[j][col+1] == 1:
                    while col < 99 and ladder[j][col+1] != 0:
                        col += 1
                        cnt += 1

            if min_count >= cnt:
                min_count = cnt
                result = i
    print(f'#{tc} {result}')
