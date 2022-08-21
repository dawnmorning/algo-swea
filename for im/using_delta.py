dr = [0,1,0,-1]
dc = [1,0,-1,0]
for i in range(m):
    for j in range(m):
        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]
            if 0<= nr < n and 0 <= nc < n:
