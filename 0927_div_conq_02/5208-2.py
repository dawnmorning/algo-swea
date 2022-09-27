import sys
sys.stdin = open('5208.txt')
T = int(input())
for tc in range(1, T+1):
    M = list(map(int, input().split()))
    N = M[0]
    cnt = -1        # 1번 정류장일 때는 세지 않으므로 미리 1을 빼줌

    loc = N
    while loc > 1:
        for i in range(loc-1, 0, -1):
            if i + M[i] >= loc:
                idx = i
        else:
            cnt += 1
            loc = idx
    print(f'#{tc} {cnt}')