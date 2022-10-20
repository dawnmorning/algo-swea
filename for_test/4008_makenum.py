def dfs(a,num, add, sub,mul,div):
    global mn,mx
    if a == n:
        mn = min(mn,num)
        mx = max(mx,num)
        return
    if add : dfs(a+1, num+lst[a],add-1,sub,mul,div)
    if sub: dfs(a + 1, num - lst[a], add, sub-1, mul, div)
    if mul: dfs(a + 1, num * lst[a], add , sub, mul-1, div)
    if div: dfs(a + 1, int(num / lst[a]), add , sub, mul, div-1)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    add, sub , mul , div = map(int, input().split())
    lst = list(map(int, input().split()))

    mn = int(1e8)
    mx = int(-1e8)
    dfs(1, lst[0], add,sub,mul,div)
    print(f'#{tc} {mx-mn}')