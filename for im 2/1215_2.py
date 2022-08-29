import sys
sys.stdin = open('1215.txt')
t = 10
for tc in range(1, t+1):
    find = int(input())
    arr = [list(map(str, input()))for _ in range(8)]
    cnt = 0
    for i in range(8):
        for j in range(8-find+1):
            if arr[i][j:j+find] == arr[i][j:j+find][::-1]:
                cnt +=1
    rev_arr = list(zip(*arr))
    for i in range(8):
        for j in range(8-find+1):
            if rev_arr[i][j:j+find] == rev_arr[i][j:j+find][::-1]:
                cnt += 1
    print(f'#{tc} {cnt}')