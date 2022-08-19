import sys
sys.stdin = open('5356.txt')
t = int(input())
for tc in range(1, t+1):
    arr = [list(map(str, input()))for _ in range(5)]
    real=[]
    for row in range(15):
        for col in range(5):
            if row < len(arr[col]):
                real += arr[col][row]
    print(f'#{tc}', end = ' ')
    for i in real:
        print(i, end='')
    print()
