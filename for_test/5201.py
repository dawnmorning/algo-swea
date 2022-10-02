import sys
sys.stdin = open('5201.txt')
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w = sorted(w, reverse=True)
    t = sorted(t, reverse= True)
    idx = value = 0
    for i in range(len(w)):
        if w[i] <= t[idx]:
            value += w[i]
            idx += 1
            if i == m-1:
                break
    print(f'#{tc} {value}')