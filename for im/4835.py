import sys
sys.stdin = open('4835.txt')
t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = list(map(int,input().split()))
    arr_list=[]
    for j in range(n-m+1):
        arr_list.append(sum(arr[j:j+m]))
    print(f'#{tc} {max(arr_list) - min(arr_list)}')

t = int(input())
for case in range(1, t+1):
    n, m = map(int, input().split())
    value = list(map(int,input().split()))
    min_value =  m * 100000
    max_value = 0
    for i in range(n-m+1):
        result = 0
        for j in range(m):
            result += value[i+j]
        if min_value > result:
            min_value = result
        if max_value < result:
            max_value = result
    print(f'#{case} {max_value - min_value}')