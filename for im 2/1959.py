import sys
sys.stdin = open('1959.txt')
t = int(input())
for tc in range(1, t+1):
    n, m = map(int,input().split())
    ai = list(map(int, input().split()))
    bj = list(map(int, input().split()))
    max_value = 0
    if n < m :
        n ,m = m, n
    if len(ai) > len(bj):
        ai, bj = bj, ai
    for i in range(n-m+1):
        lotate_value = 0
        for j in range(m):
            lotate_value += ai[j] * bj[j+i]
        if max_value < lotate_value:
            max_value = lotate_value
    print(f'#{tc} {max_value}')