import sys
sys.stdin = open('5356.txt')
t = int(input())
for tc in range(1, t+1):
    talking = [list(input())for _ in range(5)]
    value = []
    for i in range(5):
        for j in range(15):
            if j < len(talking[i]):
                value += talking[j][i]

