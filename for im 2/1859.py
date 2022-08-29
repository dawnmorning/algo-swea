import sys
sys.stdin = open('1859.txt')
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    kimsundal = list(map(int, input().split()))
    max_sell = 0
    margin = 0
    for i in range(len(kimsundal)-1,-1,-1):
        if max_sell > kimsundal[i]:
            margin += max_sell - kimsundal[i]
        else:
            max_sell = kimsundal[i]
    print(f'#{tc} {margin}')
