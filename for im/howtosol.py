import sys
sys.stdin = open('howotosol.txt')
n, m = map(int, input().split())
wall = [[0]*n for _ in range(m)]
n = int(input())
for i in range(n):
    r1,c1,r2,c2,color = map(int,input().split())
    for j in range(r1,r2+1):
        for k in range(c1,c2+1):
            if color < wall[j][k]:
                break
            else:
                wall[j][k] = color

cnt = [0] *11
for a in range(12):
    for b in range(m):
        for c in range(n):
            if wall[b][c] == a:
                cnt[a] += 1
print(cnt)




