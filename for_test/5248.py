import sys
sys.stdin = open('5248.txt')

def findset(x):
    while rep_list[x] != x:
        x = rep_list[x]
    return rep_list[x]

def union(x,y):
    rep_list[findset(y)] = findset(x)
t = int(input())
for tc in range(1,t +1):
    n, m = map(int, input().split())
    rep_list = [i for i in range(n+1)]
    temp = list(map(int, input().split()))
    for k in range(m):
        a, b = temp[2*k], temp[2*k + 1]
        union(a,b)
    ans = set()
    for i in rep_list:
        ans.add(findset(i))
    print(f'#{tc} {len(ans)-1}')