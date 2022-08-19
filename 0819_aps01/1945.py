import sys
sys.stdin = open('1945.txt')
t = int(input())
for tc in range(1, t+1):
    value = int(input())
    arr = [0] * 5
    nanum = [2,3,5,7,11]
    for i in range(len(nanum)):
        while value % nanum[i] == 0:
            arr[i] += 1
            value = value // nanum[i]
    print(f'#{tc}',*arr)