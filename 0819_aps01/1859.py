import sys
sys.stdin = open('1859.txt')
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    value = list(map(int,input().split()))
    max_day = 0
    margin = 0
    for i in range(len(value)-1,-1,-1):
        if max_day > value[i]:
            margin += max_day - value[i]
        else:
            max_day = value[i]
    print(f'#{tc} {margin}')