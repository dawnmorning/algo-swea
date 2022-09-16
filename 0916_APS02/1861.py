import sys
sys.stdin = open('1861.txt')
def dfs(row,col):
    st = [(row,col)]
    cnt = 0
    while st:
        row, col = st.pop()
        cnt += 1
        dr = [-1,1,0,0]
        dc = [0,0,1,-1]
        for i in range(4):
            nr, nc = row + dr[i], col + dc[i]
            if 0 <= nr < n and 0 <= nc < n and li[nr][nc] - li[row][col] ==1:
                st.append((nr,nc))
    return cnt
t = int(input())
for tc in range(1, t+1) :
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    maxV = -123456789
    for row in range(n):
        for col in range(n):
            cnt = dfs(row,col)
            if cnt > maxV:
                maxV = cnt
                room = [li[row][col]]
            elif cnt == maxV:
                room.append(li[row][col])  # [1, 3]
    print(f'#{tc} {min(room)} {maxV}')
