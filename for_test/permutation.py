def dfs(V):
    if V == r:
        print(result)
    else:
        for i in range(len(num)):
            if check[i] == 0:
                check[i] = 1
                result[V] = num[i]
                dfs(V+1)
                check[i] = 0

num = [1,2,3,4]
r = 3
check = [0] * len(num)
result = [0] * r
dfs(0)

