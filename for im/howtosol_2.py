import sys
sys.stdin = open('howtosol_2.txt')
n = int(input())
taebaek = [[0]*(n+2)] + [[0] + list(map(int,input().split())) + [0] for _ in range(n)] + [[0] * (n+2)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]
result = 0
for i in range(1, n+1):
    for j in range(1,n+1):
        cnt = 0
        for k in range(4):
            next_r = i + dr[k]
            next_c = j + dc[k]
            if taebaek[i][j] > taebaek[next_r][next_c]:
                cnt += 1
            if cnt == 4:
                result += 1
print(result)

# import sys
# sys.stdin = open('howtosol_2.txt')
n = int(input())
mountain = [[0] * (n+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(n)] + [[0] * (n+2)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]
result = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        cnt = 0
        for k in range(4):
            move_r = i + dr[k]
            move_c = j + dc[k]
            if mountain[i][j] > mountain[move_r][move_c]:
                cnt += 1
            if cnt == 4:
                result += 1
print(result)