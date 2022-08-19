import sys
sys.stdin = open('1966.txt')
t = int(input())
for tc in range(1, t+1):
    counting = int(input())
    sorting = list(map(int, input().split()))
    for i in range(len(sorting)-1,0,-1):
        for j in range(i):
            if sorting[j] > sorting[j+1] :
                sorting[j], sorting[j+1] = sorting[j+1], sorting[j]
    print(f'#{tc}', *sorting)
