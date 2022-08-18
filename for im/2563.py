import sys
input = sys.stdin.readline
arr = [[0] * 100 for _ in range(100)]
n = int(input())
for tc in range(n):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            arr[i][j] += 1
    cnt = 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] > 0:
                cnt += 1
print(cnt)

#간단하게 생각하기
#뭘 겹치고 빼고 이런거 X