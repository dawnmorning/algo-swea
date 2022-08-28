import sys
sys.stdin = open('1209.txt')
t = 10
for tc in range(1, t+1):
    a = input()
    arr = [list(map(int, input().split()))for _ in range(100)]
    most_sum = 0
    for i in range(100):
        sumR = 0
        sumC = 0
        sumD = 0
        sumD += arr[i][i]
        for j in range(100):
            sumR += arr[i][j]
            sumC += arr[j][i]
        if sumR > most_sum:
            most_sum = sumR
        if sumC > most_sum:
            most_sum = sumC
        if sumD > most_sum:
            most_sum = sumD
    print(f'#{tc} {most_sum}')
