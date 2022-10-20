import sys
sys.stdin = open('imdaebi.txt')
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(input())for _ in range(n+1))]
    for row in range(n+1):
        for col in range(n):
            if arr[row][col] == 'A':
                k = 1
            if arr[row][col] == 'B':
                k = 2
            if arr[row][col] == 'C':
                k = 2

            for k in range(k + 1):
                    # k 범위 안의 h를 '-'로 바꾼다
    cnt = 0
    for row in range(n+1):
        for col in range(n):
            if arr[row][col] == "H":
                cnt += 1

