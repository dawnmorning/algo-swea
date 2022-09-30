import sys
sys.stdin = open('1251.txt')

def findset(x):
    while x != rep[x]:
        x = rep[x]
    return x

def union(x,y):
    rep[findset(y)] = findset(x)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    coordinate = [[] for _ in range(n)]
    for i in range(n):
        coordinate[i] = [x[i], y[i]]
    E = float(input())
    rep = [a for a in range(n+1)]
    edge = []
    for i in range(n):
        for j in range(n):
            if i < j:
                edge.append([ (coordinate[i][0] - coordinate[j][0]) ** 2 + (coordinate[i][1] - coordinate[j][1]) ** 2 , i, j] )
                # edge.append([e * ((coordinate[i][0] - coordinate[j][0]) ** 2 + (coordinate[i][1] - coordinate[j][1]) ** 2),i, j])
    # print(edge)
    edge.sort()
    cnt = 0
    total = 0
    for w,s,e in edge:
        if findset(s) != findset(e):
            cnt += 1
            union(s,e)
            total += w
            if cnt == n:
                break
    print(f'#{tc} {(E * total):.0f}')