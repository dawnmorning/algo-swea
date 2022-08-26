import sys
sys.stdin = open('1226.txt')

def bfs(row,col):
    # 인접 정점을 확인하기 위한 델타
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    q = []
    q.append((row,col)) #한 쌍으로 들어가야 하기 때문
    visited[row][col] = 1 # 방문처리
    #인접한 정점을 찾는다
    while q:  # q가 비어있지 않을 때, 반복
        # 1. 큐에서 데이터를 가져온다.
        r, c = q.pop(0)
        visited[r][c] = 1
        # 2. 인접한 정점을 찾는다.
        for idx in range(4): # 상 하 좌 우 4방향 탐색
            next_row = r + dr[idx]
            next_col = c + dc[idx]
            # 16*16사이즈를 혹시 벗어나지 않았는지 check (그렇지 않으면 out of range)
            if 0 <= next_row < 16 and 0 <= next_col <16:
        # 3. 방문 가능하다면 q에 넣는다.
                # 벽이 아니고, 내가 왔던 길이 아니라면 방문가능한 길
                if map_data[next_row][next_col] != 1 and visited[next_row][next_col] != 1: # 3까지 가야하므로 == 0 이 아니라 !=1이라고 해야함)
                    if map_data[next_row][next_col] == 3: # 혹시 도착점이라면 1을 리턴
                        return 1
                    q.append((next_row, next_col))
                    # 만약 이동거리까지 필요하다면
                    visited[next_row][next_col] = visited[r][c] + 1
    return 0


def find_start(map_data):
    for r in range(16):
        for c in range(16):
            if map_data[r][c] == 2:
                return r,c        # 시작점 받아오기

t= 10
for tc in range(1, t+1):
    tc = input()
    map_data = [list(map(int, input()))for _ in range(16)] #미로를 저장
    visited = [[0] * 16 for _ in range(16)] # 방문 리스트
    row, col = find_start(map_data)
    result = bfs(row,col)
    print(f'#{tc} {result}')