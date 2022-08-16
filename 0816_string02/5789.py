import sys
sys.stdin = open('5789.txt')
t = int(input())
for tc in range(1, t+1):
    n,q = map(int, input().split())
    arr = ['0'] * n
    for i in range(1,q+1):
        L, R = map(int,input().split())
        for j in range(L-1, R):
            arr[j] = str(i)
    print(f'#{tc}', ' '.join(arr))