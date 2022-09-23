import sys
sys.stdin = open('2819.txt')

def dfs(r,c, value):
    global value_li
    if len(value) == 7:
        if value not in value_li:
            value_li.append(value)
        return
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, value+str(arr[nr][nc]))

t = int(input())
for tc in range(1, t+1):
    arr = [list(input().split())for _ in range(4)]
    value_li = []

    for i in range(4):
        for j in range(4):
            dfs(i,j, arr[i][j])
    print(f'#{tc} {len(value_li)}')

