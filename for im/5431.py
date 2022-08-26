import sys
sys.stdin = open('5431.txt')
t = int(input())
for tc in range(1, t+1):
    n, k = map(int,input().split())
    submit_num = list(map(int,input().split()))
    check_num = []
    for i in range(1, n+1):
        if i not in submit_num:
            check_num.append(i)
    print(f'#{tc}',end = ' ')
    for j in check_num:
        print(j,end = ' ')
    print()

