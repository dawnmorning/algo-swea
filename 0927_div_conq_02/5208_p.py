import sys
sys.stdin = open('5208.txt')
t = int(input())

def dfs(now, gas, cnt):
    global result
    # 현재 위치가 도착지를 벗어난다면(충분히 도착 가능한 경우)
    if now >= len(station) - 1:
        if cnt < result:
            result = cnt
    else:
        if gas > 0 :
            dfs(now+1, gas-1, cnt)
        # 가지치기 : 아직 충전횟수가 더 적다면 배터리 충전
        if cnt < result:
            dfs(now+1, station[now]-1 ,cnt +1)

for tc in range(1, t+1):
    # 0번째 : 정류장 수 / 1 ~ n-1 정류장별 충전지
    arr = list(map(int, input().split()))
    station = arr[1:] + [0]  # n번 반복을 위해 0 추가
    result = arr[0] # 초기 값은 정류장 마다 배터리를 교체하는 경우
    dfs(1, station[0]-1, 0) # 현재 정류장 위치, 남은 배터리, 배터리 교체 횟수
    print(f'#{tc} {result}')
