import sys
sys.stdin = open('5249.txt')

def findset(x):
    while x != rep_list[x]:
        x = rep_list[x]
    return x

def union(x,y):
    rep_list[findset(y)] = findset(x)

t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    adjlist = []
    for _ in range(e):
        n1, n2, w = map(int, input().split())
        adjlist.append([n1,n2,w])
    adjlist.sort(key=lambda x : x[2])
    rep_list = [i for i in range(v+1)]

    n = v+1
    cnt = 0
    total = 0
    for n1, n2, w in adjlist:
        if findset(n1) != findset(n2):
            cnt += 1
            union(n1,n2)
            total += w
            if cnt == n-1:
                break
    print(f'#{tc} {total}')

