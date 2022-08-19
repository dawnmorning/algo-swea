# import sys
# sys.stdin = open('1979.txt')
# t = int(input())
# for tc in range(1, t+1):
#     n, k = map(int,input().split())
#     puzzle = [list(map(int, input().split()))for _ in range(n)]
#     result = 0
#     for i in range(n):
#         cnt = 0
#         for j in range(n):
#             if puzzle[i][j] == 1:
#                 cnt += 1
#             if puzzle[i][j] == 0 or j == n-1:
#                 if cnt == k:
#                     result += 1
#                 if puzzle[i][j] == 0:
#                     cnt = 0
#     print(f'#{tc} {result}')
import sys
sys.stdin = open('1979.txt')
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(n)] #  # 이차원 리스트로 받아옴
    result = 0  #최종 결과값을 위한 자리
    for i in range(n):
        cnt = 0  # 1이 있을 때 마다 카운트 올리기
        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
            if arr[i][j] == 0 or j == n-1:  # 자리가 0이거나 마지막 자리까지 갔을 때, cnt가 우리가 찾으려는 m 길이라면,
                if cnt == m :
                    result += 1  #result를 +1 해준다
                if arr[i][j] == 0:  # 인덱스 진행 때 중간에 0이 들어가서 m자리만큼 채울 수 없게 되므로, 0으로 바꿔줘야 한다. 그렇지 않으면 [1,1,0,1]도 cnt = 3으로 잡힘
                    cnt = 0
    for i in range(n):
        cnt = 0 
        for j in range(n):
            if arr[j][i] == 1:
                cnt += 1
            if arr[j][i] == 0 or j == n-1:
                if cnt == m :
                    result += 1
                if arr[j][i] == 0:
                    cnt = 0
    print(f'#{tc} {result}')