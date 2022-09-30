


t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int, input().split()))for _ in range(n)]
    minV = 99999
    dr = [0,1]
    dc = [1,0]
    start = arr[0][0]
    dfs(0,0,start)





