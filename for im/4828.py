import sys
sys.stdin = open('4828.txt')
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    minV = 9999999
    maxV = 0
    for i in range(n):
        if maxV < arr[i]:
            maxV = arr[i]
        if minV > arr[i]:
            minV = arr[i]
    print(f'#{tc} {maxV - minV}')