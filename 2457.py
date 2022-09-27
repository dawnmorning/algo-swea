import sys
sys.stdin = open('2457.txt')
t = 2
for tc in range(1, t+1):
    n = int(input())
    date = []
    for _  in range(n):
        temp = list(map(int, input().split()))
        date.append([temp * 100 + temp[1], temp[2] * 100 + temp[3]])
    date.sort(key= lambda x : (x[0], x[1]))
    cnt = 0
