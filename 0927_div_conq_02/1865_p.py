import sys
sys.stdin = open('1865.txt')

def search(worker, value):
    global result

    if result >= value:  # 현재 저장된 효율보다 계산된 효율이 더 낮다면 다음 일을 줘도 효율이 낮을 것
       return

    if worker == n:
        result = value
        return
    else:
        for i in range(n):
            if visited[i] == 0:  # 현재 일하는 중이 아니라면
                visited[i] = 1
                search(worker+1, value*arr[worker][i])
                visited[i] = 0


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 정수를 퍼센트로 변경 소수형태로.
    for i in range(n):
        for j in range(n):
            arr[i][j] = arr[i][j] / 100

    # dfs 준비
    visited = [0] * n
    result = 0
    search(0, 1)
    print(f'#{tc} {result*100:6f}')