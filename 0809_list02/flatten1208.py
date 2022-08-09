import sys
sys.stdin = open('flatten.txt')
t = 10
for case in range(1, t+1):
    value = int(input())
    box = list(map(int, input().split()))
    while(value):
        for i in range(99, 0, -1):
            for j in range(i):
                if box[j] > box[j+1]:
                    box[j], box[j+1] = box[j+1], box[j]
        box[0] += 1
        box[99] -= 1
        value -= 1
    for i in range(99, 0, -1):
        for j in range(i):
            if box[j] > box[j + 1]:
                box[j], box[j + 1] = box[j + 1], box[j]
    print(f'#{case} {box[99] - box[0]}')

