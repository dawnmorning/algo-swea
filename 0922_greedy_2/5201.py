import sys
sys.stdin = open('5201.txt')
t = int(input())
for tc in range(1, t+1):
    n, m = map(int,input().split())
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))
    wi.sort(reverse = True)
    ti.sort(reverse = True)
    idx = value = 0
    for w in wi:
        if w <= ti[idx]:
            value += w
            idx += 1
        if idx == m :  #  없으면 out of range
            break
    print(f'#{tc} {value}')
