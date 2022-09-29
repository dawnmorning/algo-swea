import sys
sys.stdin = open('5250.txt')

def dfs():
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    inf = 10 ** 6
    # 최단거리로 바꿀 배열
    visited = [[inf] * n for _ in range(n)]
    # 시작점은 제일 처음이라고 했으니, 0,0 부터 시작
    visited[0][0] = 0
    q = []
    # 시작점 큐에 넣고
    q.append((0,0))
    # 돌려
    while q:
        value = q.pop(0)
        for k in range(4):
            nr = value[0] + dr[k]
            nc = value[1] + dc[k]
            if nr >= 0 and nr < n and nc >= 0 and nc < n:
                subs = 0    # 높이 차이 값, substract
                # 기존 높이 기록 한 배열에서 높이 차이가 있다면, 차이만큼 더해줘야해서
                if height[nr][nc] > height[value[0]][value[1]]:
                    # 차이 먼저 구해줌
                    subs = height[nr][nc] - height[value[0]][value[1]]
                    # 최소값으로 바꿔주는 과정
                if visited[nr][nc] > visited[value[0]][value[1]] + subs + 1 :
                    visited[nr][nc] = visited[value[0]][value[1]] + subs + 1
                    q.append((nr,nc))
    return visited[n-1][n-1]
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    height = [list(map(int, input().split())) for _ in range(n)]
    print(f'#{tc} {dfs()}')
