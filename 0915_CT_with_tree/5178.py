import sys
sys.stdin = open('5178.txt')
t = int(input())
for tc in range(1, t+1):
    n, m, l = map(int, input().split())
    par = [0] * (n+1)
    for i in range(m):
        tree = list(map(int, input().split()))
        idx, value = tree[0], tree[1]
        par[idx] = value
    for j in range(n-m, 0, -1):
        try:
            par[j] = par[2*j] + par[2*j+1]
        except:
            par[j] = par[2*j]
    print(f'#{tc} {par[l]}')


