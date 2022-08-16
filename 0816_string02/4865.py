import sys
sys.stdin = open('4865.txt')
t = int(input())
for tc in range(1, t+1):
    str_1 = list(map(str,input()))
    str_2 = list(map(str,input()))
    arr = [0] * len(str_1)
    for i in range(len(str_1)):
        for j in range(len(str_2)):
            if str_1[i] == str_2[j]:
                arr[i] += 1
    value = 0
    for k in range(len(str_1)):
        if arr[k] > value:
            value = arr[k]
    print(f'#{tc} {value}')
