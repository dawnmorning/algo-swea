import sys
sys.stdin = open('5249.txt')

def findset(x):
    while x != rep_list[x]:
        x = rep_list[x]
    return rep_list[x]

def union(x,y):
    rep_list[findset(y)] = findset(x)

    if x < y :
        rep_list[y] = x
    else:
        rep_list[x] = y


t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(e)]
    rep_list = [i for i in range(v+1)]
    info.sort(key=lambda x : x[2])
    cnt = 0
    value = 0
    for s,e,c in info:
        if findset(s) != findset(e):
            cnt += 1
            value += c
            union(s,e)
            if cnt == v:
                break
    print(f'#{tc} {value}')

