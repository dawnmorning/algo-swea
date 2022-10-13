import sys
sys.stdin = open('5656.txt')
import copy

def dfs(idx, mapss):
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    global break_cnt
    if idx == n:
        cnt = 0
        for z in range(h):
            cnt += mapss[z].count(0)
        temp = w*h - cnt
        if temp < break_cnt:
            break_cnt = temp
        return

    for col in range(w):
        for row in range(h):
            if mapss[row][col] == 0:
                continue
            else:
                copy_maps = copy.deepcopy(mapss)
                q = [(row,col,mapss[row][col])]
                while q:
                    v = q.pop(0)
                    if v[2] == 1:
                        mapss[v[0]][v[1]] = 0
                    else:
                        mapss[v[0]][v[1]] = 0
                        for k in range(1, v[2]):
                            for i in range(4):
                                nr = v[0] + dr[i] * k
                                nc = v[1] + dc[i] * k
                                if 0 <= nr < h and 0 <= nc < w and mapss[nr][nc] != 0:
                                    if(nr, nc , mapss[nr][nc]) not in q:
                                        q.append((nr, nc , mapss[nr][nc]))
                new_map = [[0 for _ in range(w)] for _ in range(h)]
                for j in range(w):
                    li = []
                    for i in range(h):
                        if mapss[i][j]:
                            li.append(mapss[i][j])
                    for a in range(len(li)):
                        new_map[h-len(li)+a][j] = li[a]
                flag = True
            if flag == 1:
                dfs(idx+1,new_map)
                mapss = copy_maps
                break
    dfs(n, mapss)



t = int(input())
for tc in range(1, t+1):
    n ,w, h = map(int, input().split())
    maps = [list(map(int, input().split()))for _ in range(h)]
    break_cnt = 9876543210
    dfs(0, maps)
    print(f'#{tc} {break_cnt}')