import sys
sys.stdin = open('5177.txt')
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    node = [0] + list(map(int,input().split()))
    value = 0
    for i in range(1, n+1):
        while node[i//2] > node[i]:
            node[i//2] , node[i] = node[i], node[i//2]
            i = i // 2
    par = n // 2
    while par >0:
        value += node[par]
        par = par // 2
    print(f'#{tc} {value}')