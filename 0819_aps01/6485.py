import sys
sys.stdin = open('6485.txt')
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [0] * 5000
    for _ in range(n):
        a, b = list(map(int, input().split()))
        for i in range(a-1, b):
            arr[i] += 1
    p = int(input())
    print(f'#{tc}', end=' ')
    for j in range(p):
        c = int(input())
        print(arr[c-1], end=' ')
    print()

