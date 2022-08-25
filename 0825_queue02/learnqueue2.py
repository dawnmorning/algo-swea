import sys
sys.stdin = open('5097.txt')
t = int(input())
for tc in range(1,t+1):
    n, m = map(int,input().split())
    arr = list(map(int,input().split()))
    for i in range(m):
        temporary = arr.pop(0)
        arr.append(temporary)
    print(f'#{tc} {arr[0]}')