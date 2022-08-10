import sys
sys.stdin = open('input1.txt')
n = int(input())


for tc in range(1, n+1):
    maxv = 0
    cnt = 0
    num = int(input())
    li = list(map(int, input()))
    for i in range(num):
        if li[i] == 1:
            cnt += 1
            if maxv < cnt:
                maxv = cnt
        else:
             cnt = 0
    print(f'#{tc} {maxv}')