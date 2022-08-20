import sys
sys.stdin = open('1959.txt')
t = int(input())
for tc in range(1, t+1):
    n, m = map(int,input().split())
    ai = list(map(int,input().split()))
    bj = list(map(int,input().split()))

    if n > m:
        ai, bj = bj, ai
        n,m = m,n

    max_value = []
    for i in range(m-n+1):
        value = []
        for k in range(n):
            # value = value + (ai[k] * bj[k+i])
            value.append(ai[k] * bj[k+i])
        max_value.append(sum(value))
    print(f'#{tc} {max(max_value)}')

