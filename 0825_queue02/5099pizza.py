import sys
sys.stdin = open('5099')
t = int(input())
for tc in range(1, t+1):
    n, m = map(int,input().split())
    cheese = list(map(int,input().split()))
    oven = []
    idx = 0
    for i in range(n):
        idx += 1
        oven.append([idx,cheese.pop(0)])


    while len(oven) != 1:
        check = oven.pop(0)
        if check[1] // 2 != 0:
            oven.append([check[0], check[1] //2])
        else:
            if cheese:
                idx += 1
                oven.append([idx, cheese.pop(0)])
    print(f'#{tc} {oven[0][0]}')