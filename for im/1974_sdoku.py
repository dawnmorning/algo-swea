import sys
sys.stdin = open('1974.txt')
t = int(input())
n = 9
m = 3

for tc in range(1, t+1):
    sdoku = [list(map(int,input().split()))for _ in range(9)]
    cnt = 0
    # 가로
    for i in range(9):
        now_multi_row = 1
        now_multi_col = 1
        for j in range(9):
            now_multi_row = now_multi_row * sdoku[i][j]
            now_multi_col = now_multi_col * sdoku[j][i]
            if now_multi_row == now_multi_col == 362880:
                cnt += 1
                break
    # 3*3
    for i in range(0,n-m+1,3):
        for j in range(0,n-m+1,3):
            now_multi = 1
            for k in range(3):
                for l in range(3):
                    now_multi = now_multi * sdoku[i+k][j+l]
                    if now_multi == 362880:
                        cnt += 1
                        break
    if cnt == 18 :
        print(f'#{tc}',1)
    else:
        print(f'#{tc}',0)
