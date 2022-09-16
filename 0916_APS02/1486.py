import sys
sys.stdin = open('1486.txt')
from itertools import combinations
t = int(input())
for tc in range(1, t+1):
    n,b = map(int, input().split())
    h = list(map(int, input().split()))
    beyond = []
    hap = []
    for i in range(n+1):
        beyond.append(list(combinations(h,i)))
        for j in range(len(beyond[i])):
            if sum(beyond[i][j]) >= b:
                hap.append(sum(beyond[i][j]))
    print(f'#{tc} {min(hap)- b}')
