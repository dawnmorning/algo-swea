import sys
sys.stdin = open('5431.txt')
t = int(input())
for tc in range(1, t+1):
    n, k = map(int,input().split())
    submit = list(map(int, input().split()))
    check = [0] * n
    for i in submit:
        check[i-1] = 1
    cut = []
    for j,k in enumerate(check):
        if k == 0:
            cut.append(j+1)
    print(f'#{tc}',*cut)

