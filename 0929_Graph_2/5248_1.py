import sys
sys.stdin = open('5248.txt')

def findset(x):
    if x == rep_list[x]:
        return x
    else:
        return findset(rep_list[x])

def union(a,b):
    rep_list[findset(b)] = findset(a)

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    hope = list(map(int, input().split()))
    rep_list = [i for i in range(n+1)]
    for j in range(len(hope)//2):
        a, b = hope[2*j], hope[2*j + 1]
        union(a,b)
    for k in range(1, n+1):
        rep_list[k] = findset(k)
    print(f'#{tc} {len(set(rep_list))-1}')