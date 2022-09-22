import sys
sys.stdin = open('5202.txt')
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    time = [list(map(int, input().split()))for _ in range(n)]
    time = sorted(time)
    time = sorted(time, key = lambda x : x[1])
    truck = 0
    compare = 0
    for i in range(n):
        if compare <= time[i][0]:
            compare = time[i][1]
            truck += 1
    print(f'#{tc} {truck}')