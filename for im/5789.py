import sys
sys.stdin = open('5789.txt')
t = int(input())
for tc in range(1, t+1):
    n, q = map(int, input().split())
    arr = [0 for _ in range(n)]
    for i in range(1, q+1):
        l, r = map(int,input().split())
        for j in range(l-1,r):
            arr[j] = i
    print(f'#{tc}', end = ' ')
    for j in range(len(arr)):
        print(arr[j], end = ' ')
    print()